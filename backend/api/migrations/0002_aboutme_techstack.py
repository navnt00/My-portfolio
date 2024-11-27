# Generated by Django 4.2 on 2024-11-16 07:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutMe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "title",
                    models.CharField(
                        help_text="e.g., Full Stack Developer", max_length=200
                    ),
                ),
                ("profile_image", models.ImageField(upload_to="profile/")),
                ("bio", models.TextField()),
                ("resume", models.FileField(blank=True, upload_to="resume/")),
                ("github", models.URLField(blank=True)),
                ("linkedin", models.URLField(blank=True)),
                ("twitter", models.URLField(blank=True)),
                ("email", models.EmailField(max_length=254)),
                ("location", models.CharField(max_length=100)),
                ("years_of_experience", models.IntegerField(default=0)),
                ("projects_completed", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name_plural": "About Me",
            },
        ),
        migrations.CreateModel(
            name="TechStack",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("frontend", "Frontend"),
                            ("backend", "Backend"),
                            ("tools", "Tools & Others"),
                        ],
                        max_length=50,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("icon", models.ImageField(upload_to="tech_icons/")),
                ("order", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name_plural": "Tech Stack",
                "ordering": ["category", "order"],
            },
        ),
    ]
