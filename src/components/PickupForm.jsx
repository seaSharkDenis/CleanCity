import React, { useState } from 'react';
import PropTypes from 'prop-types';

const PickupForm = ({ onSubmit }) => {
  const [formData, setFormData] = useState({
    address: '',
    date: '',
  });

  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const validate = () => {
    const newErrors = {};
    if (!formData.address.trim()) newErrors.address = 'Address is required';
    if (!formData.date.trim()) newErrors.date = 'Date is required';
    return newErrors;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const validationErrors = validate();
    setErrors(validationErrors);
    if (Object.keys(validationErrors).length === 0 && onSubmit) {
      onSubmit(formData);
    }
  };

  return (
    <form onSubmit={handleSubmit} aria-label="pickup-form">
      <div>
        <label htmlFor="address">Pickup Address:</label>
        <input
          id="address"
          name="address"
          value={formData.address}
          onChange={handleChange}
        />
        {errors.address && <p>{errors.address}</p>}
      </div>
      <div>
        <label htmlFor="date">Pickup Date:</label>
        <input
          id="date"
          name="date"
          type="date"
          value={formData.date}
          onChange={handleChange}
        />
        {errors.date && <p>{errors.date}</p>}
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};
PickupForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
};

export default PickupForm;
