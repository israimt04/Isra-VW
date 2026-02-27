# Registration Form Application

A React-based registration form application built with Vite that allows users to register with their details and view a personalized dashboard.

## Features

- **Registration Form**: Users can enter their name, email, phone number, and address
- **Form Validation**: All fields are validated before submission
- **Details Display**: After registration, users can see their details on a dashboard
- **Welcome Message**: Personalized welcome message showing the user's name
- **Logout Functionality**: Users can logout and return to the registration form

## Project Structure

```
src/
├── components/
│   ├── RegistrationForm.jsx      # Registration form component
│   ├── RegistrationForm.css      # Form styling
│   ├── DisplayDetails.jsx        # Details display component
│   └── DisplayDetails.css        # Details page styling
├── App.jsx                       # Main app component
├── App.css                       # App styling
├── main.jsx                      # React entry point
└── index.css                     # Global styles
```

## Technology Stack

- **React** 18.2.0
- **Vite** 5.0.8 (Build tool)
- **JavaScript/JSX**
- **CSS3**

## Installation

1. Navigate to the project directory:
```bash
cd /Users/israimtiyaz/Desktop/Volkswagen/Training/Training-2/Isra-VW/Assignments/15Day
```

2. Install dependencies:
```bash
npm install
```

## Running the Application

Start the development server:
```bash
npm run dev
```

The application will be available at `http://localhost:3000`

## Building for Production

Create a production build:
```bash
npm run build
```

Preview the production build:
```bash
npm run preview
```

## How to Use

1. **Registration**: Fill out the registration form with your details:
   - Name (required)
   - Email (required, must be valid email)
   - Phone Number (required, must be 10 digits)
   - Address (required)

2. **Submit**: Click the "Register" button to submit your details

3. **View Details**: Your registered details will be displayed on the dashboard page with a personalized welcome message

4. **Logout**: Click the "Logout" button in the top right corner to return to the registration form

## Validation Rules

- **Name**: Cannot be empty
- **Email**: Must be a valid email format
- **Phone Number**: Must be exactly 10 digits
- **Address**: Cannot be empty

Error messages will appear below each field if validation fails.

## Browser Compatibility

Works on all modern browsers that support ES6+ and modern CSS features.
