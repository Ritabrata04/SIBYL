'use client'
import React, { useState } from 'react';
import './page.css';
const ContactPage = () => {
  const [formData, setFormData] = useState({
    experienceYears: '',
    educationLevel: '',
    name: '',
    jobTitle: '',
    age: '',
    numberOfSwitches: '',
    careerSwitches: '', // default value for the dropdown
  });
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };



  const handleSubmit = (e) => {
    e.preventDefault();
    // Add your form submission logic here
    console.log('Form submitted:', formData);
  };

  return (
    <div>

      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <br />
          <input type="text" name="name" value={formData.name} onChange={handleChange} />
        </label>
        <label>
          Age:
          <br />
          <input type="text" name="age" value={formData.age} onChange={handleChange} />
        </label>
        <label>
          Number of Switches:
          <br />
          <input
            type="text"
            name="numberOfSwitches"
            value={formData.numberOfSwitches}
            onChange={handleChange}
          />
        </label>




        <label>
          Job Title:
          <br />

          <select name="jobTitle" value={formData.jobTitle} onChange={handleChange}>
            <option value="">Select Job Title</option>
            <option value="Data Scientist">Data Scientist</option>
            <option value="Product Manager">Product Manager</option>
            <option value="DevOps Engineer">DevOps Engineer</option>
            <option value="Software Engineer">Software Engineer</option>
            <option value="System Analyst">System Analyst</option>

          </select>
        </label>

        <label>
          Education Level:
          <br />
          <select name="educationLevel" value={formData.educationLevel} onChange={handleChange}>
            <option value="">Select Education Level</option>
            <option value="Bachelor">Bachelor's</option>
            <option value="Master">Master's</option>
            <option value="PhD">Ph.D</option>
          </select>
        </label>

        <label>
          Experience years:
          <br />
          <input type="text" name="experienceYears" value={formData.experienceYears} onChange={handleChange} />
        </label>


        {/* Career Switches */}


        <button className="submitbtn" type="submit">Submit</button>
      </form>

      {/* Display the career switch list */}
      {Array.isArray(formData.careerSwitches) && formData.careerSwitches.length > 0 && (
        <div>
          <h2>The Career Options You Can Switch Into:</h2>
          <ul>
            {formData.careerSwitches.slice(0, 5).map((career, index) => (
              <li key={index}>{career}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default ContactPage

