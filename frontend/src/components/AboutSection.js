import React from 'react';

function AboutSection({ aboutMe }) {
  return (
    <div className="card">
      <div className="flex flex-col md:flex-row items-center gap-8 mb-8">
        <div className="w-full md:w-2/3">
          <p className="text-gray-600 leading-relaxed">
            {aboutMe.bio}
          </p>
          <div className="mt-6 flex gap-4">
            {aboutMe.github && (
              <a href={aboutMe.github} target="_blank" rel="noopener noreferrer" className="text-gray-600 hover:text-primary">
                GitHub
              </a>
            )}
            {aboutMe.linkedin && (
              <a href={aboutMe.linkedin} target="_blank" rel="noopener noreferrer" className="text-gray-600 hover:text-primary">
                LinkedIn
              </a>
            )}
            {aboutMe.twitter && (
              <a href={aboutMe.twitter} target="_blank" rel="noopener noreferrer" className="text-gray-600 hover:text-primary">
                Twitter
              </a>
            )}
          </div>
        </div>
        <div className="w-full md:w-1/3">
          <div className="bg-gray-100 rounded-lg p-6">
            <div className="mb-4">
              <p className="text-gray-600">
                <span className="font-bold">Location:</span> {aboutMe.location}
              </p>
            </div>
            <div className="mb-4">
              <p className="text-gray-600">
                <span className="font-bold">Experience:</span> {aboutMe.years_of_experience} years
              </p>
            </div>
            <div>
              <p className="text-gray-600">
                <span className="font-bold">Projects:</span> {aboutMe.projects_completed}+ completed
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default AboutSection; 