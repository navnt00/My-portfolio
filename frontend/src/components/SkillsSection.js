import React from 'react';
import { Link } from 'react-router-dom';

function SkillsSection({ skills }) {
  return (
    <section className="bg-gray-100 py-20">
      <div className="container mx-auto px-4">
        <h2 className="section-title text-center">My Skills</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
          {skills.map((skill) => (
            <div key={skill.id} className="bg-white rounded-xl shadow-lg p-6 hover:shadow-xl transition-shadow duration-300">
              <div className="flex items-center mb-4">
                {skill.icon && (
                  <img
                    src={skill.icon}
                    alt={skill.name}
                    className="w-12 h-12 object-contain mr-4"
                  />
                )}
                <h3 className="text-xl font-bold text-gray-800">
                  {skill.name}
                </h3>
              </div>
              
              <div className="space-y-2">
                <div className="flex justify-between items-center mb-1">
                  <span className="text-sm font-medium text-gray-600">
                    Proficiency
                  </span>
                  <span className="text-sm font-medium text-primary">
                    {skill.proficiency}/5
                  </span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2.5">
                  <div
                    className="bg-primary h-2.5 rounded-full transition-all duration-500"
                    style={{ width: `${(skill.proficiency / 5) * 100}%` }}
                  ></div>
                </div>
              </div>
            </div>
          ))}
        </div>
        <div className="text-center mt-8">
          <Link 
            to="/skills"
            className="inline-block px-6 py-3 bg-primary text-white rounded-lg hover:bg-blue-700 transition-colors"
          >
            View All Skills →
          </Link>
        </div>
      </div>
    </section>
  );
}

export default SkillsSection; 