import React from 'react';
import { Link } from 'react-router-dom';

function ProjectsSection({ projects }) {
  return (
    <section className="bg-gray-100 py-20">
      <div className="container mx-auto px-4">
        <h2 className="section-title text-center">Featured Projects</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {projects.map((project) => (
            <div key={project.id} className="bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300">
              <div className="relative pb-[60%]">
                <img
                  src={project.image}
                  alt={project.title}
                  className="absolute h-full w-full object-cover"
                />
              </div>
              
              <div className="p-6">
                <h3 className="text-xl font-bold text-gray-800 mb-2">
                  {project.title}
                </h3>
                <p className="text-gray-600 mb-4">
                  {project.description}
                </p>
                <div className="mb-4">
                  <h4 className="text-sm font-semibold text-gray-700 mb-2">Technologies:</h4>
                  <div className="flex flex-wrap gap-2">
                    {project.technologies.split(',').map((tech, index) => (
                      <span
                        key={index}
                        className="px-3 py-1 bg-blue-100 text-blue-600 rounded-full text-sm"
                      >
                        {tech.trim()}
                      </span>
                    ))}
                  </div>
                </div>
                <div className="flex justify-between items-center">
                  {project.github_link && (
                    <a
                      href={project.github_link}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-primary hover:text-blue-700 transition-colors"
                    >
                      GitHub →
                    </a>
                  )}
                  {project.live_link && (
                    <a
                      href={project.live_link}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="btn-primary"
                    >
                      Live Demo
                    </a>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
        <div className="text-center mt-8">
          <Link 
            to="/projects"
            className="inline-block px-6 py-3 bg-primary text-white rounded-lg hover:bg-blue-700 transition-colors"
          >
            View All Projects →
          </Link>
        </div>
      </div>
    </section>
  );
}

export default ProjectsSection;