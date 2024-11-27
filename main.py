import os
import cv2
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras import backend as K

# Directories
dir_images = '../input/satellite-images-of-water-bodies/Water Bodies Dataset/Images'
dir_masks = '../input/satellite-images-of-water-bodies/Water Bodies Dataset/Masks'

# Collect image and mask paths
image_paths = [os.path.join(dir_images, fname) for fname in os.listdir(dir_images)]
mask_paths = [os.path.join(dir_masks, fname) for fname in os.listdir(dir_masks)]

# DataFrame for paths
data = pd.DataFrame({"image_path": image_paths, "mask_path": mask_paths})

# Image size
IMG_SIZE = [256, 256]

# Data augmentation and preprocessing functions
def data_augmentation(image, mask):
    if tf.random.uniform(()) > 0.5:
        image = tf.image.flip_left_right(image)
        mask = tf.image.flip_left_right(mask)
    return image, mask

def preprocess(image_path, mask_path):
    # Image
    image = tf.io.read_file(image_path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, IMG_SIZE)
    image = tf.cast(image, tf.float32) / 255.0

    # Mask
    mask = tf.io.read_file(mask_path)
    mask = tf.image.decode_jpeg(mask, channels=1)
    mask = tf.image.resize(mask, IMG_SIZE)
    mask = tf.cast(mask > 0, tf.float32)  # Convert to binary

    return image, mask

# Split dataset and create TensorFlow datasets
train_data, valid_data = train_test_split(data, test_size=0.25, random_state=42)

def create_dataset(df, augment=False):
    dataset = tf.data.Dataset.from_tensor_slices((df["image_path"].values, df["mask_path"].values))
    dataset = dataset.map(preprocess, num_parallel_calls=tf.data.AUTOTUNE)
    if augment:
        dataset = dataset.map(data_augmentation, num_parallel_calls=tf.data.AUTOTUNE)
    return dataset.batch(16).prefetch(tf.data.AUTOTUNE)

train_dataset = create_dataset(train_data, augment=True)
valid_dataset = create_dataset(valid_data)

# Define U-Net model with MobileNetV2 backbone
base_model = tf.keras.applications.MobileNetV2(input_shape=[256, 256, 3], include_top=False)
layer_names = ['block_1_expand_relu', 'block_3_expand_relu', 'block_6_expand_relu', 'block_13_expand_relu', 'block_16_project']
base_outputs = [base_model.get_layer(name).output for name in layer_names]
down_stack = tf.keras.Model(inputs=base_model.input, outputs=base_outputs)
down_stack.trainable = False

def upsample(filters, size):
    return tf.keras.Sequential([
        tf.keras.layers.Conv2DTranspose(filters, size, strides=2, padding='same'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.ReLU()
    ])

up_stack = [upsample(512, 3), upsample(256, 3), upsample(128, 3), upsample(64, 3)]

def unet_model(output_channels):
    inputs = tf.keras.layers.Input(shape=[256, 256, 3])
    x = inputs
    skips = down_stack(x)
    x = skips[-1]
    skips = reversed(skips[:-1])

    for up, skip in zip(up_stack, skips):
        x = up(x)
        x = tf.keras.layers.Concatenate()([x, skip])

    x = tf.keras.layers.Conv2DTranspose(output_channels, 3, strides=2, padding='same', activation='sigmoid')
    return tf.keras.Model(inputs=inputs, outputs=x)

model = unet_model(1)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Training
EPOCHS = 40
STEPS_PER_EPOCH = len(train_data) // 16
early_stop = tf.keras.callbacks.EarlyStopping(patience=4, restore_best_weights=True)

history = model.fit(train_dataset,
                    epochs=EPOCHS,
                    steps_per_epoch=STEPS_PER_EPOCH,
                    validation_data=valid_dataset,
                    callbacks=[early_stop])

# Visualization function
def display(display_list):
    plt.figure(figsize=(12, 12))
    titles = ['Input Image', 'True Mask', 'Predicted Mask']
    for i in range(len(display_list)):
        plt.subplot(1, len(display_list), i + 1)
        plt.title(titles[i])
        plt.imshow(tf.keras.preprocessing.image.array_to_img(display_list[i]))
        plt.axis('off')
    plt.show()

def show_predictions(dataset, num=1):
    for image, mask in dataset.take(num):
        pred_mask = model.predict(image)
        display([image[0], mask[0], pred_mask[0]])

# Show predictions
show_predictions(valid_dataset, num=3)
