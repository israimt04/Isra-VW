import './DisplayDetails.css'

function DisplayDetails({ userDetails, onLogout }) {
  return (
    <div className="display-container">
      <header className="header">
        <h1 className="app-title">Dashboard</h1>
        <div className="user-section">
          <span className="welcome-message">Welcome, {userDetails.name}!</span>
          <button onClick={onLogout} className="logout-btn">Logout</button>
        </div>
      </header>

      <div className="details-wrapper">
        <h2>Your Registered Details</h2>
        <div className="details-card">
          <div className="detail-item">
            <label className="detail-label">Name:</label>
            <p className="detail-value">{userDetails.name}</p>
          </div>

          <div className="detail-item">
            <label className="detail-label">Email:</label>
            <p className="detail-value">{userDetails.email}</p>
          </div>

          <div className="detail-item">
            <label className="detail-label">Phone Number:</label>
            <p className="detail-value">{userDetails.phno}</p>
          </div>

          <div className="detail-item">
            <label className="detail-label">Address:</label>
            <p className="detail-value">{userDetails.address}</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default DisplayDetails
