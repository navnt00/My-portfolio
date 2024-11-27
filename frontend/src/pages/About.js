import React, { useState, useEffect } from 'react';
import axios from 'axios';

function About() {
  const [aboutMe, setAboutMe] = useState(null);
  const [techStack, setTechStack] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/about/')
      .then(response => {
        if (response.data.length > 0) {
          setAboutMe(response.data[0]);
        }
      })
      .catch(error => console.error('Error fetching about me:', error));

    axios.get('http://localhost:8000/api/tech-stack/')
      .then(response => {
        const groupedTech = response.data.reduce((acc, item) => {
          if (!acc[item.category]) {
            acc[item.category] = [];
          }
          acc[item.category].push(item);
          return acc;
        }, {});
        setTechStack(groupedTech);
      })
      .catch(error => console.error('Error fetching tech stack:', error));
  }, []);

  if (!aboutMe) {
    return <div>Loading...</div>;
  }

  return (
    <div className="min-h-screen bg-gray-50 py-12">
      <div className="container mx-auto px-4">
        <div className="max-w-4xl mx-auto">
          {/* Profile Section */}
          <div className="bg-white rounded-xl shadow-lg overflow-hidden mb-8">
            <div className="bg-gradient-to-r from-primary to-blue-700 p-8 text-center">
              <img
                src={aboutMe.profile_image}
                alt={aboutMe.name}
                className="w-80 h-80 rounded-full border-4 border-white mx-auto mb-4 object-cover"
              />
              <h1 className="text-3xl font-bold text-white mb-2">{aboutMe.name}</h1>
              <p className="text-white opacity-90">{aboutMe.title}</p>
            </div>
            
            <div className="p-8">
              <div className="prose max-w-none">
                <p className="text-gray-600 leading-relaxed mb-6">{aboutMe.bio}</p>
              </div>

              {/* Stats */}
              <div className="grid grid-cols-2 md:grid-cols-3 gap-6 mb-8">
                <div className="text-center">
                  <div className="text-2xl font-bold text-primary">{aboutMe.years_of_experience}+</div>
                  <div className="text-gray-600">Years Experience</div>
                </div>
                <div className="text-center">
                  <div className="text-2xl font-bold text-primary">{aboutMe.projects_completed}+</div>
                  <div className="text-gray-600">Projects Completed</div>
                </div>
                <div className="text-center md:col-span-1 col-span-2">
                  <div className="text-2xl font-bold text-primary">{aboutMe.location}</div>
                  <div className="text-gray-600">Location</div>
                </div>
              </div>

              {/* Social Links */}
              <div className="flex justify-center gap-6">
                {aboutMe.github && (
                  <a
                    href={aboutMe.github}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-gray-600 hover:text-primary transition-colors"
                  >
                    GitHub
                  </a>
                )}
                {aboutMe.linkedin && (
                  <a
                    href={aboutMe.linkedin}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-gray-600 hover:text-primary transition-colors"
                  >
                    LinkedIn
                  </a>
                )}
                {aboutMe.twitter && (
                  <a
                    href={aboutMe.twitter}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-gray-600 hover:text-primary transition-colors"
                  >
                    Twitter
                  </a>
                )}
              </div>
            </div>
          </div>

          {/* Tech Stack Section */}
          <div className="bg-white rounded-xl shadow-lg p-8">
            <h2 className="text-2xl font-bold text-gray-800 mb-6 text-center">
              Technical Skills
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              {Object.entries(techStack).map(([category, technologies]) => (
                <div key={category} className="space-y-4">
                  <h3 className="text-lg font-semibold text-primary capitalize">
                    {category}
                  </h3>
                  <div className="space-y-2">
                    {technologies.map((tech) => (
                      <div key={tech.id} className="flex items-center gap-2 bg-gray-50 p-2 rounded">
                        <img
                          src={tech.icon}
                          alt={tech.name}
                          className="w-6 h-6 object-contain"
                        />
                        <span className="text-gray-700">{tech.name}</span>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default About; 