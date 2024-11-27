import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function Navbar() {
  const [isOpen, setIsOpen] = useState(false);
  const [aboutMe, setAboutMe] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/api/about/')
      .then(response => {
        if (response.data.length > 0) {
          setAboutMe(response.data[0]);
        }
      })
      .catch(error => console.error('Error fetching about me:', error));
  }, []);

  return (
    <nav className="bg-white shadow-lg sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link to="/" className="flex items-center">
              {aboutMe?.profile_image ? (
                <img
                  src={aboutMe.profile_image}
                  alt={aboutMe.name}
                  className="h-10 w-10 rounded-full object-cover border-2 border-primary"
                />
              ) : (
                <div className="h-10 w-10 rounded-full bg-primary flex items-center justify-center text-white font-bold">
                  NY
                </div>
              )}
              <span className="ml-2 text-lg font-semibold text-gray-800 hidden sm:block">
                {aboutMe?.name || 'Portfolio'}
              </span>
            </Link>
          </div>

          {/* Desktop Menu */}
          <div className="hidden md:flex items-center space-x-4">
            <Link to="/" className="text-gray-700 hover:text-primary px-3 py-2 rounded-md">
              Home
            </Link>
            <Link to="/about" className="text-gray-700 hover:text-primary px-3 py-2 rounded-md">
              About
            </Link>
            <Link to="/projects" className="text-gray-700 hover:text-primary px-3 py-2 rounded-md">
              Projects
            </Link>
            <Link to="/skills" className="text-gray-700 hover:text-primary px-3 py-2 rounded-md">
              Skills
            </Link>
            <Link to="/contact" className="btn-primary">
              Contact
            </Link>
          </div>

          {/* Mobile Menu Button */}
          <div className="md:hidden flex items-center">
            <button
              onClick={() => setIsOpen(!isOpen)}
              className="text-gray-700 hover:text-primary focus:outline-none"
            >
              <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                {isOpen ? (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                ) : (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                )}
              </svg>
            </button>
          </div>
        </div>

        {/* Mobile Menu */}
        {isOpen && (
          <div className="md:hidden">
            <div className="px-2 pt-2 pb-3 space-y-1">
              <Link
                to="/"
                className="block text-gray-700 hover:text-primary px-3 py-2 rounded-md"
                onClick={() => setIsOpen(false)}
              >
                Home
              </Link>
              <Link
                to="/about"
                className="block text-gray-700 hover:text-primary px-3 py-2 rounded-md"
                onClick={() => setIsOpen(false)}
              >
                About
              </Link>
              <Link
                to="/projects"
                className="block text-gray-700 hover:text-primary px-3 py-2 rounded-md"
                onClick={() => setIsOpen(false)}
              >
                Projects
              </Link>
              <Link
                to="/skills"
                className="block text-gray-700 hover:text-primary px-3 py-2 rounded-md"
                onClick={() => setIsOpen(false)}
              >
                Skills
              </Link>
              <Link
                to="/contact"
                className="block text-gray-700 hover:text-primary px-3 py-2 rounded-md"
                onClick={() => setIsOpen(false)}
              >
                Contact
              </Link>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
}

export default Navbar;