# Railway Management API

## Overview
The Railway Management API is a Flask-based backend system that allows users to register, book train tickets, and manage railway operations efficiently. The system includes authentication, train management, and seat booking functionalities.

## Features
- **User Authentication**: Register and login with JWT-based authentication.
- **Admin Panel**: Secure train management operations.
- **Train Management**: Retrieve available trains based on source and destination.
- **Seat Booking**: Users can book available seats on a train.

## Installation

### Prerequisites
Ensure you have Python installed (preferably Python 3.8+), along with PostgreSQL as the database.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/RailwayManagementAPI.git
   cd RailwayManagementAPI
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   - Update `config.py` with your PostgreSQL credentials.
   - Run migrations:
     ```bash
     flask db init
     flask db migrate -m "Initial migration"
     flask db upgrade
     ```
5. Run the application:
   ```bash
   flask run
   ```
6. The API will be available at: `http://127.0.0.1:5000/`

## API Endpoints
### Authentication
- `POST /register` - Register a new user.
- `POST /login` - Login and receive a JWT token.

### Admin Routes
- `POST /admin/train` - Add a new train (Requires Admin API Key).

### User Routes
- `GET /trains?source=SOURCE&destination=DEST` - Get available trains.
- `POST /book` - Book a seat on a train (Requires authentication).

## Running Tests
To run the test cases, use:
```bash
pytest tests/
```
