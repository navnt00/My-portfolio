import React from 'react';

function TechStack({ techStack }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
      {Object.entries(techStack).map(([category, technologies]) => (
        <div key={category} className="text-center">
          <h3 className="font-bold text-lg text-primary mb-4 capitalize">
            {category}
          </h3>
          <div className="flex flex-wrap justify-center gap-3">
            {technologies.map((tech) => (
              <div key={tech.id} className="flex items-center">
                <img
                  src={tech.icon}
                  alt={tech.name}
                  className="w-6 h-6 mr-2"
                />
                <span className="text-gray-600">{tech.name}</span>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}

export default TechStack; 