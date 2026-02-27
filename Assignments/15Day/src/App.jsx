import { useState } from 'react'
import RegistrationForm from './components/RegistrationForm'
import DisplayDetails from './components/DisplayDetails'
import './App.css'

function App() {
  const [isRegistered, setIsRegistered] = useState(false)
  const [userDetails, setUserDetails] = useState(null)

  const handleRegistration = (details) => {
    setUserDetails(details)
    setIsRegistered(true)
  }

  const handleLogout = () => {
    setIsRegistered(false)
    setUserDetails(null)
  }

  return (
    <>
      {!isRegistered ? (
        <RegistrationForm onRegister={handleRegistration} />
      ) : (
        <DisplayDetails userDetails={userDetails} onLogout={handleLogout} />
      )}
    </>
  )
}

export default App
