import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import PickupForm from './PickupForm';

describe('PickupForm', () => {
  test('renders all required fields', () => {
    render(<PickupForm />);
    expect(screen.getByLabelText(/pickup address/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/pickup date/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /submit/i })).toBeInTheDocument();
  });

  test('shows validation errors when fields are empty', () => {
    render(<PickupForm />);
    fireEvent.click(screen.getByRole('button', { name: /submit/i }));
    expect(screen.getByText(/address is required/i)).toBeInTheDocument();
    expect(screen.getByText(/date is required/i)).toBeInTheDocument();
  });

  test('calls onSubmit with form data when form is valid', () => {
    const handleSubmit = jest.fn();
    render(<PickupForm onSubmit={handleSubmit} />);

    fireEvent.change(screen.getByLabelText(/pickup address/i), {
      target: { value: '123 Main St' },
    });
    fireEvent.change(screen.getByLabelText(/pickup date/i), {
      target: { value: '2025-07-20' },
    });

    fireEvent.click(screen.getByRole('button', { name: /submit/i }));
    expect(handleSubmit).toHaveBeenCalledWith({
      address: '123 Main St',
      date: '2025-07-20',
    });
  });
});

