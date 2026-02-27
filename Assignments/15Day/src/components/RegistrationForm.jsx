import { useState } from 'react'
import './RegistrationForm.css'

function RegistrationForm({ onRegister }) {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phno: '',
    address: ''
  })

  const [errors, setErrors] = useState({})

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData({
      ...formData,
      [name]: value
    })
    // Clear error for this field
    if (errors[name]) {
      setErrors({
        ...errors,
        [name]: ''
      })
    }
  }

  const validateForm = () => {
    const newErrors = {}

    if (!formData.name.trim()) {
      newErrors.name = 'Name is required'
    }

    if (!formData.email.trim()) {
      newErrors.email = 'Email is required'
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      newErrors.email = 'Please enter a valid email'
    }

    if (!formData.phno.trim()) {
      newErrors.phno = 'Phone number is required'
    } else if (!/^\d{10}$/.test(formData.phno.replace(/\D/g, ''))) {
      newErrors.phno = 'Please enter a valid 10-digit phone number'
    }

    if (!formData.address.trim()) {
      newErrors.address = 'Address is required'
    }

    setErrors(newErrors)
    return Object.keys(newErrors).length === 0
  }

  const handleSubmit = (e) => {
    e.preventDefault()

    if (validateForm()) {
      onRegister(formData)
      setFormData({
        name: '',
        email: '',
        phno: '',
        address: ''
      })
    }
  }

  return (
    <div className="registration-container">
      <div className="form-wrapper">
        <h1>Registration Form</h1>
        <form onSubmit={handleSubmit} className="registration-form">
          <div className="form-group">
            <label htmlFor="name">Name:</label>
            <input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              placeholder="Enter your full name"
            />
            {errors.name && <span className="error">{errors.name}</span>}
          </div>

          <div className="form-group">
            <label htmlFor="email">Email:</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="Enter your email"
            />
            {errors.email && <span className="error">{errors.email}</span>}
          </div>

          <div className="form-group">
            <label htmlFor="phno">Phone Number:</label>
            <input
              type="tel"
              id="phno"
              name="phno"
              value={formData.phno}
              onChange={handleChange}
              placeholder="Enter your phone number"
            />
            {errors.phno && <span className="error">{errors.phno}</span>}
          </div>

          <div className="form-group">
            <label htmlFor="address">Address:</label>
            <textarea
              id="address"
              name="address"
              value={formData.address}
              onChange={handleChange}
              placeholder="Enter your address"
              rows="4"
            ></textarea>
            {errors.address && <span className="error">{errors.address}</span>}
          </div>

          <button type="submit" className="submit-btn">Register</button>
        </form>
      </div>
    </div>
  )
}

export default RegistrationForm
