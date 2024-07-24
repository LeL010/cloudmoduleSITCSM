import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../App.css';

const ContactUs = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
  });

  const history = useHistory();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('http://busgpt-alb-1547579194.us-east-1.elb.amazonaws.com/api/contact', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    });
    if (response.ok) {
      alert('Message sent successfully!');
      setFormData({
        name: '',
        email: '',
        message: ''
      });
      history.push('/contact-us');
    } else {
      alert('Failed to send message.');
    }
  };

  return (
    <div className="section">
      <h1 className="title">Contact Us</h1>
      <form onSubmit={handleSubmit}>
        <div className="field">
          <label className="label">Name</label>
          <div className="control">
            <input className="input" type="text" name="name" value={formData.name} onChange={handleChange} required />
          </div>
        </div>
        <div className="field">
          <label className="label">Email</label>
          <div className="control">
            <input className="input" type="email" name="email" value={formData.email} onChange={handleChange} required />
          </div>
        </div>
        <div className="field">
          <label className="label">Message</label>
          <div className="control">
            <textarea className="textarea" name="message" value={formData.message} onChange={handleChange} required />
          </div>
        </div>
        <div className="control">
          <button className="button is-primary" type="submit">Submit</button>
        </div>
      </form>
    </div>
  );
};

export default ContactUs;
