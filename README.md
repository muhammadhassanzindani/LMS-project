# LMS Project

A simple Learning Management System with Django backend and React frontend, using MongoDB with mongoengine ODM.

## Prerequisites

- Python 3.8+
- Node.js 14+
- MongoDB (local installation or MongoDB Atlas)

## Quick Start

### Step 1: Clone and Setup Environment

```bash
# Navigate to project directory
cd LMS-project

# Copy environment file
cp .env.example .env

# Edit .env file with your MongoDB connection details
nano .env  # or use your preferred editor
```

### Step 2: Configure Environment Variables

Edit the `.env` file with your MongoDB configuration:

**Option 1: Using Connection URI (Recommended)**
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=*

# MongoDB Connection URI
DB_CONNECTION=mongodb://localhost:27017/
DATABASE=LMS-Project
```

**Option 2: Using Individual Settings**
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=*

# MongoDB Individual Settings
MONGODB_HOST=localhost
MONGODB_PORT=27017
MONGODB_USERNAME=
MONGODB_PASSWORD=
DATABASE=LMS-Project
```

**For MongoDB Atlas (Cloud):**
```env
DB_CONNECTION=mongodb+srv://username:password@cluster.mongodb.net/
DATABASE=LMS-Project
```

### Step 3: Setup MongoDB

**Local MongoDB:**
```bash
# Install MongoDB (if not installed)
# macOS: brew install mongodb-community
# Ubuntu: sudo apt-get install mongodb
# Windows: Download from mongodb.com

# Start MongoDB service
mongod  # or brew services start mongodb-community (macOS)
```

**MongoDB Atlas (Cloud):**
- Sign up at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- Create a free cluster
- Get your connection string
- Add it to `.env` as `DB_CONNECTION`

### Step 4: Setup Backend (Django)

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (recommended)
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install Python dependencies
pip install -r ../requirements.txt

# Start Django development server
python manage.py runserver
```

The backend API will be running at `http://localhost:8000`

**Note:** With mongoengine, you don't need to run migrations like traditional Django models.

### Step 5: Setup Frontend (React)

Open a **new terminal window** and run:

```bash
# Navigate to frontend directory
cd frontend

# Install Node.js dependencies
npm install

# Start React development server
npm start
```

The frontend will automatically open at `http://localhost:3000`

## How to Run the Project

### Running Backend Only

```bash
cd backend
source venv/bin/activate  # Activate virtual environment
python manage.py runserver
```

Backend will be available at: `http://localhost:8000`
API endpoints: `http://localhost:8000/api/courses/`

### Running Frontend Only

```bash
cd frontend
npm start
```

Frontend will be available at: `http://localhost:3000`

### Running Both (Recommended)

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate
python manage.py runserver
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```

Then open your browser and navigate to `http://localhost:3000`

## Project Structure

```
LMS-project/
├── backend/
│   ├── lms_project/       # Django project settings
│   ├── courses/           # Courses app with models, views, serializers
│   ├── manage.py          # Django management script
│   └── ...
├── frontend/
│   ├── src/               # React source files
│   ├── public/            # Public HTML files
│   ├── package.json       # Node.js dependencies
│   └── ...
├── .env                   # Environment variables (create from .env.example)
├── .env.example           # Environment variables template
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Features

- ✅ Create new courses
- ✅ View all courses
- ✅ Edit existing courses
- ✅ Delete courses
- ✅ Simple, clean interface
- ✅ MongoDB database with mongoengine ODM
- ✅ Environment variables configuration
- ✅ Wildcard CORS enabled (allows all origins)
- ✅ Connection URI support for MongoDB Atlas

## API Endpoints

- `GET /api/courses/` - List all courses
- `POST /api/courses/` - Create a new course
- `GET /api/courses/{id}/` - Get a specific course
- `PUT /api/courses/{id}/` - Update a course
- `DELETE /api/courses/{id}/` - Delete a course

## Environment Variables

All configuration is stored in `.env` file:

### Required Variables

- `SECRET_KEY` - Django secret key for security
- `DEBUG` - Debug mode (True/False)
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts (use `*` for all)
- `DATABASE` - MongoDB database name (default: `LMS-Project`)

### MongoDB Configuration

**Option 1: Connection URI (Recommended)**
- `DB_CONNECTION` - MongoDB connection URI
  - Local: `mongodb://localhost:27017/`
  - Atlas: `mongodb+srv://username:password@cluster.mongodb.net/`

**Option 2: Individual Settings**
- `MONGODB_HOST` - MongoDB host (default: localhost)
- `MONGODB_PORT` - MongoDB port (default: 27017)
- `MONGODB_USERNAME` - MongoDB username (optional)
- `MONGODB_PASSWORD` - MongoDB password (optional)

### CORS Configuration

- CORS is set to allow all origins (wildcard) by default
- No additional configuration needed

## Troubleshooting

### MongoDB Connection Issues

1. **Check if MongoDB is running:**
   ```bash
   # Check MongoDB status
   mongosh  # or mongo (older versions)
   ```

2. **Verify connection string in `.env`:**
   - For local: `DB_CONNECTION=mongodb://localhost:27017/`
   - For Atlas: Use the connection string from Atlas dashboard

3. **Check firewall settings** if using remote MongoDB

### Backend Issues

1. **Virtual environment not activated:**
   ```bash
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

2. **Dependencies not installed:**
   ```bash
   pip install -r ../requirements.txt
   ```

3. **Port 8000 already in use:**
   ```bash
   python manage.py runserver 8080  # Use different port
   ```

### Frontend Issues

1. **Node modules not installed:**
   ```bash
   npm install
   ```

2. **Port 3000 already in use:**
   - React will automatically suggest using a different port
   - Or set `PORT=3001 npm start`

3. **CORS errors:**
   - Backend has wildcard CORS enabled, should work automatically
   - Check that backend is running on port 8000

## Development

### Adding New Features

1. **Backend (Django):**
   - Add models in `backend/courses/models.py`
   - Add serializers in `backend/courses/serializers.py`
   - Add views in `backend/courses/views.py`
   - Update URLs in `backend/courses/urls.py`

2. **Frontend (React):**
   - Add components in `frontend/src/`
   - Update `frontend/src/App.js` to use new components

### Database

- Database name: `LMS-Project` (as specified in `DATABASE` env variable)
- Collections are created automatically by mongoengine
- No migrations needed

## License

This project is for educational purposes.
