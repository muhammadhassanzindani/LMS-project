# LMS Project (Windows Setup)

A simple Learning Management System with a **Django backend** and **React frontend**, using **MongoDB** with **mongoengine ODM**.

---

## Prerequisites (Windows)

* **Windows 10 / 11**
* **Python 3.8+** (make sure *Add Python to PATH* is checked during installation)
* **Node.js 14+** (includes npm)
* **MongoDB** (Local installation **or** MongoDB Atlas)
* **Git** (optional but recommended)

---

## Quick Start (Windows)

### Step 1: Clone and Setup Environment

Open **Command Prompt** or **PowerShell**:

```bat
cd LMS-project

copy .env.example .env
```

Open `.env` in **Notepad / VS Code** and update MongoDB details.

---

### Step 2: Configure Environment Variables

Edit the `.env` file:

#### Option 1: Using MongoDB Connection URI (Recommended)

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=*

DB_CONNECTION=mongodb://localhost:27017/
DATABASE=LMS-Project
```

#### Option 2: Using Individual MongoDB Settings

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=*

MONGODB_HOST=localhost
MONGODB_PORT=27017
MONGODB_USERNAME=
MONGODB_PASSWORD=
DATABASE=LMS-Project
```

#### MongoDB Atlas (Cloud)

```env
DB_CONNECTION=mongodb+srv://username:password@cluster.mongodb.net/
DATABASE=LMS-Project
```

---

### Step 3: Setup MongoDB

#### Option A: Local MongoDB (Windows)

1. Download MongoDB Community Server from:
   [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)
2. Install with default settings
3. Make sure **MongoDB Service** is running

Verify installation:

```bat
mongosh
```

#### Option B: MongoDB Atlas (Cloud)

* Create a free cluster at MongoDB Atlas
* Get the connection string
* Paste it into `.env` as `DB_CONNECTION`

---

### Step 4: Setup Backend (Django)

```bat

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

python -m venv venv

venv\Scripts\activate

pip install -r ..\requirements.txt

cd backend

python manage.py runserver
```

Backend will run at:

```
http://localhost:8000
```

> ⚠️ **Note:** No Django migrations are required because MongoDB is used via mongoengine.

---

### Step 5: Setup Frontend (React)

Open **another Command Prompt / PowerShell window**:

```bat
cd frontend

npm install

npm start
```

Frontend will open at:

```
http://localhost:3000
```

---

## Running the Project

### Backend Only

```bat
cd backend
venv\Scripts\activate
python manage.py runserver
```

### Frontend Only

```bat
cd frontend
npm start
```

### Recommended: Run Both

**Terminal 1 (Backend):**

```bat
cd backend
venv\Scripts\activate
python manage.py runserver
```

**Terminal 2 (Frontend):**

```bat
cd frontend
npm start
```

Open browser:

```
http://localhost:3000
```

---

## Project Structure

```
LMS-project/
├── backend/
│   ├── lms_project/
│   ├── courses/
│   ├── manage.py
│   └── ...
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
├── .env
├── .env.example
├── requirements.txt
└── README.md
```

---

## Features

* Create, view, edit, and delete courses
* Django REST backend
* React frontend
* MongoDB with mongoengine
* MongoDB Atlas support
* Environment-based configuration
* Wildcard CORS enabled

---

## API Endpoints

* `GET /api/courses/`
* `POST /api/courses/`
* `GET /api/courses/{id}/`
* `PUT /api/courses/{id}/`
* `DELETE /api/courses/{id}/`

---

## Troubleshooting (Windows)

### MongoDB Not Connecting

```bat
mongosh
```

* Ensure MongoDB service is running
* Verify `.env` connection string

---

### Backend Issues

* Activate virtual environment:

```bat
venv\Scripts\activate
```

* Install dependencies:

```bat
pip install -r ..\requirements.txt
```

* Change port if 8000 is busy:

```bat
python manage.py runserver 8080
```

---

### Frontend Issues

* Install packages:

```bat
npm install
```

* Change port:

```bat
set PORT=3001 && npm start
```

---

## Development Notes

### Backend

* Models: `backend/courses/models.py`
* Views: `backend/courses/views.py`
* URLs: `backend/courses/urls.py`

### Frontend

* Components: `frontend/src/`
* Entry point: `frontend/src/App.js`

---

