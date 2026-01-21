import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

// Backend URL from environment variable (REACT_APP_ prefix required for React)
// Add REACT_APP_BACKEND_URL to your .env file in the frontend directory
const BACKEND_URL = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8000';
const API_URL = `${BACKEND_URL}/api/courses/`;

function App() {
  // State for storing list of courses
  const [courses, setCourses] = useState([]);
  
  // State for tracking which course is being edited
  const [editingCourse, setEditingCourse] = useState(null);
  
  // State for loading indicator
  const [loading, setLoading] = useState(false);
  
  // State for error messages
  const [error, setError] = useState(null);
  
  // State for form input data
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    instructor: ''
  });

  // Fetch courses when component mounts
  useEffect(() => {
    fetchCourses();
  }, []);

  // Fetch all courses from backend API
  const fetchCourses = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.get(API_URL);
      if (response.data.success) {
        setCourses(response.data.data || []);
      } else {
        setError(response.data.error || 'Failed to fetch courses');
      }
    } catch (error) {
      setError(error.response?.data?.error || error.message || 'Error fetching courses');
      console.error('Error fetching courses:', error);
    } finally {
      setLoading(false);
    }
  };

  // Handle form input changes
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    setError(null);
  };

  // Handle form submission (create or update course)
  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    
    try {
      let response;
      if (editingCourse) {
        // Update existing course
        response = await axios.put(`${API_URL}${editingCourse.id}/`, formData);
      } else {
        // Create new course
        response = await axios.post(API_URL, formData);
      }
      
      if (response.data.success) {
        // Clear form and refresh courses list
        setFormData({ title: '', description: '', instructor: '' });
        setEditingCourse(null);
        await fetchCourses();
      } else {
        setError(response.data.error || 'Failed to save course');
      }
    } catch (error) {
      const errorMsg = error.response?.data?.error || 
                      error.response?.data?.errors || 
                      error.message || 
                      'Error saving course';
      setError(errorMsg);
      console.error('Error saving course:', error);
    } finally {
      setLoading(false);
    }
  };

  // Handle edit button click
  const handleEdit = (course) => {
    setEditingCourse(course);
    setFormData({
      title: course.title,
      description: course.description,
      instructor: course.instructor
    });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Handle delete button click
  const handleDelete = async (id) => {
    if (!window.confirm('Are you sure you want to delete this course?')) {
      return;
    }
    
    setLoading(true);
    setError(null);
    try {
      const response = await axios.delete(`${API_URL}${id}/`);
      if (response.data.success) {
        await fetchCourses();
      } else {
        setError(response.data.error || 'Failed to delete course');
      }
    } catch (error) {
      const errorMsg = error.response?.data?.error || 
                      error.message || 
                      'Error deleting course';
      setError(errorMsg);
      console.error('Error deleting course:', error);
    } finally {
      setLoading(false);
    }
  };

  // Handle cancel button click (clear form)
  const handleCancel = () => {
    setFormData({ title: '', description: '', instructor: '' });
    setEditingCourse(null);
    setError(null);
  };

  return (
    <div className="app">
      <div className="container">
        <header className="app-header">
          <h1>Learning Management System</h1>
          <p className="subtitle">Course Management Dashboard</p>
        </header>
        
        {error && (
          <div className="alert alert-error">
            <span className="alert-icon">⚠️</span>
            <span>{typeof error === 'object' ? JSON.stringify(error) : error}</span>
            <button className="alert-close" onClick={() => setError(null)}>×</button>
          </div>
        )}

        <div className="form-section">
          <div className="section-header">
            <h2>{editingCourse ? '✏️ Edit Course' : '➕ Create New Course'}</h2>
            {editingCourse && (
              <button className="btn-cancel" onClick={handleCancel}>
                Cancel
              </button>
            )}
          </div>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="title">Course Title *</label>
              <input
                id="title"
                type="text"
                name="title"
                value={formData.title}
                onChange={handleInputChange}
                placeholder="Enter course title"
                required
                maxLength={200}
              />
            </div>
            <div className="form-group">
              <label htmlFor="description">Description *</label>
              <textarea
                id="description"
                name="description"
                value={formData.description}
                onChange={handleInputChange}
                placeholder="Enter course description"
                required
                rows={4}
              />
            </div>
            <div className="form-group">
              <label htmlFor="instructor">Instructor Name *</label>
              <input
                id="instructor"
                type="text"
                name="instructor"
                value={formData.instructor}
                onChange={handleInputChange}
                placeholder="Enter instructor name"
                required
                maxLength={100}
              />
            </div>
            <div className="form-actions">
              <button 
                type="submit" 
                className="btn-primary"
                disabled={loading}
              >
                {loading ? '⏳ Processing...' : (editingCourse ? '💾 Update Course' : '✨ Create Course')}
              </button>
            </div>
          </form>
        </div>

        <div className="courses-section">
          <div className="section-header">
            <h2>📚 Courses ({courses.length})</h2>
            {!loading && (
              <button className="btn-refresh" onClick={fetchCourses}>
                🔄 Refresh
              </button>
            )}
          </div>
          
          {loading && courses.length === 0 ? (
            <div className="loading-state">
              <div className="spinner"></div>
              <p>Loading courses...</p>
            </div>
          ) : courses.length === 0 ? (
            <div className="empty-state">
              <div className="empty-icon">📖</div>
              <h3>No courses yet</h3>
              <p>Create your first course using the form above</p>
            </div>
          ) : (
            <div className="courses-list">
              {courses.map(course => (
                <div key={course.id} className="course-card">
                  <div className="course-header">
                    <h3>{course.title}</h3>
                    <span className="course-badge">Active</span>
                  </div>
                  <div className="course-body">
                    <div className="course-info">
                      <span className="info-label">👨‍🏫 Instructor:</span>
                      <span className="info-value">{course.instructor}</span>
                    </div>
                    <div className="course-description">
                      <span className="info-label">📝 Description:</span>
                      <p>{course.description}</p>
                    </div>
                    {course.created_at && (
                      <div className="course-meta">
                        <small>Created: {new Date(course.created_at).toLocaleDateString()}</small>
                      </div>
                    )}
                  </div>
                  <div className="course-actions">
                    <button 
                      onClick={() => handleEdit(course)} 
                      className="btn-edit"
                      disabled={loading}
                    >
                      ✏️ Edit
                    </button>
                    <button 
                      onClick={() => handleDelete(course.id)} 
                      className="btn-delete"
                      disabled={loading}
                    >
                      🗑️ Delete
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
