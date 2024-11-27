import React, { useState, useEffect } from 'react';
import axios from 'axios';
import AboutSection from '../components/AboutSection';
import TechStack from '../components/TechStack';
import ProjectsSection from '../components/ProjectsSection';
import SkillsSection from '../components/SkillsSection';
import ContactSection from '../components/ContactSection';

function Home() {
  const [projects, setProjects] = useState([]);
  const [aboutMe, setAboutMe] = useState(null);
  const [techStack, setTechStack] = useState([]);
  const [skills, setSkills] = useState([]);
  const [isResumeLoading, setIsResumeLoading] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [projectsRes, aboutRes, techStackRes, skillsRes] = await Promise.all([
          axios.get('http://localhost:8000/api/projects/'),
          axios.get('http://localhost:8000/api/about/'),
          axios.get('http://localhost:8000/api/tech-stack/'),
          axios.get('http://localhost:8000/api/skills/')
        ]);

        setProjects(projectsRes.data);
        if (aboutRes.data.length > 0) {
          setAboutMe(aboutRes.data[0]);
        }

        const groupedTech = techStackRes.data.reduce((acc, item) => {
          if (!acc[item.category]) {
            acc[item.category] = [];
          }
          acc[item.category].push(item);
          return acc;
        }, {});
        setTechStack(groupedTech);
        
        setSkills(skillsRes.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const handleResumeClick = async () => {
    if (!aboutMe?.resume) {
      alert('Resume is not available at the moment.');
      return;
    }

    setIsResumeLoading(true);
    try {
      const fileName = aboutMe.resume.split('/').pop();
      
      const response = await axios.get(aboutMe.resume, {
        responseType: 'blob',
        headers: {
          'Accept': 'application/pdf,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        }
      });

      const blob = new Blob([response.data], { 
        type: response.headers['content-type'] 
      });
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', fileName);
      
      document.body.appendChild(link);
      
      link.click();
      
      link.parentNode.removeChild(link);
      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error('Error downloading resume:', error);
      alert('Failed to download resume. Please try again later.');
    } finally {
      setIsResumeLoading(false);
    }
  };

  if (!aboutMe) {
    return <div>Loading...</div>;
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-primary to-blue-700 text-white py-20" id="home">
        <div className="container mx-auto px-4">
          <div className="max-w-4xl mx-auto text-center">
            <div className="mb-8">
              <img
                src={aboutMe.profile_image}
                alt={aboutMe.name}
                className="w-40 h-40 rounded-full mx-auto border-4 border-white shadow-xl object-cover"
              />
            </div>
            <h1 className="text-5xl font-bold mb-6">
              Hi, I'm <span className="text-yellow-300">{aboutMe.name}</span>
            </h1>
            <p className="text-xl mb-8">
              {aboutMe.title}
            </p>
            <div className="flex justify-center gap-4">
              <a 
                href="#contact" 
                className="btn-primary scroll-smooth"
                onClick={(e) => {
                  e.preventDefault();
                  document.getElementById('contact').scrollIntoView({ behavior: 'smooth' });
                }}
              >
                Get In Touch
              </a>
              <button
                onClick={handleResumeClick}
                disabled={isResumeLoading}
                className={`px-6 py-2 bg-white text-primary rounded-lg hover:bg-gray-100 transition-colors flex items-center gap-2 ${
                  isResumeLoading ? 'opacity-50 cursor-not-allowed' : ''
                }`}
              >
                {isResumeLoading ? (
                  <svg 
                    className="w-5 h-5 animate-spin" 
                    fill="none" 
                    stroke="currentColor" 
                    viewBox="0 0 24 24"
                  >
                    <circle 
                      className="opacity-25" 
                      cx="12" 
                      cy="12" 
                      r="10" 
                      stroke="currentColor" 
                      strokeWidth="4"
                    />
                    <path 
                      className="opacity-75" 
                      fill="currentColor" 
                      d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                    />
                  </svg>
                ) : (
                  <svg 
                    className="w-5 h-5" 
                    fill="none" 
                    stroke="currentColor" 
                    viewBox="0 0 24 24"
                  >
                    <path 
                      strokeLinecap="round" 
                      strokeLinejoin="round" 
                      strokeWidth={2} 
                      d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" 
                    />
                  </svg>
                )}
                {isResumeLoading ? 'Downloading...' : 'Resume'}
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* About Section */}
      <section className="py-10" id="about">
        <div className="container mx-auto px-4">
          <h2 className="section-title text-center">About Me</h2>
          <div className="max-w-40xl mx-auto">
            <AboutSection aboutMe={aboutMe} />
          </div>
          <br />
          <div className="max-w-40xl mx-auto">
            <TechStack techStack={techStack} />
          </div>
        </div>
      </section>

      {/* Skills Section */}
      <section id="skills">
        <SkillsSection skills={skills} />
      </section>

      {/* Projects Section */}
      <section id="projects">
        <ProjectsSection projects={projects} />
      </section>

      {/* Contact Section */}
      <section id="contact">
        <ContactSection />
      </section>

      {/* Footer */}
      <footer className="bg-gray-800 text-white py-8 text-center">
        <div className="container mx-auto px-4">
          <p>© {new Date().getFullYear()} {aboutMe.name}. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
}

export default Home; 