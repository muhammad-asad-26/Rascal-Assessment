# Rascal — Django Project

This is a Django-based web application with users, subscriptions and events micro-applications.
The user app allows user to signup, login.
The subscription app allows user to add subscription plans of plan type month or year and allows user to subscribe to a plan as well as retrieve the plans.
The event app allows user to create events and subscribe to events.
The backend uses sqlite for easy development purposes.

## APIs

### Users
- POST /users/register
- POST /users/register-admin
- POST /users/login

### Subscriptions
- POST /subscriptions/add
- POST /subscriptions/subscribe/<uuid:plan>
- GET /subscriptions/all
- GET /subscriptions/me

### Events
- POST /events/create
- POST /events/subscribe/<uuid:event>

## Prerequisites
- **Python 3.10+**
- **pip** (comes with Python)

## Getting Started


### 1. Create & activate a virtual environment

```bash
# Create
python -m venv venv

# Activate (macOS / Linux)
source ../venv/bin/activate

# Activate (Windows)
..\venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run database migrations

```bash
python manage.py migrate
```

### 4. Run the development server

```bash
python manage.py runserver
```

The app will be available at **http://127.0.0.1:8000/**.



### Additional Notes for next 4 hours if awarded

What i would build if i had another 4 hours:
- Introduce JWT Authentication for securing the endpoints
- Introduce get all events endpoint to allow users to view all events and subscribe to them
- Add endpoints for admin that would allow them to view and manage the users, events and subscriptions.
- Write unit test
- Add swagger documentation