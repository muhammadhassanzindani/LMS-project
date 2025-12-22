"""
Course Model - MongoDB Document using mongoengine ODM

Similar to FastAPI Pydantic models, but using mongoengine for MongoDB.
This defines the data structure and validation rules.
"""
from mongoengine import Document, StringField, DateTimeField
from datetime import datetime


class Course(Document):
    """
    Course Document Model
    
    Fields:
        title: Course title (required, max 200 chars)
        description: Course description (required)
        instructor: Instructor name (required, max 100 chars)
        created_at: Auto-set on creation
        updated_at: Auto-updated on save
    """
    title = StringField(required=True, max_length=200)
    description = StringField(required=True)
    instructor = StringField(required=True, max_length=100)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    def save(self, *args, **kwargs):
        """Override save to auto-update timestamps"""
        if not self.created_at:
            self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        return super(Course, self).save(*args, **kwargs)

    def __str__(self):
        """String representation for admin/debugging"""
        return self.title

    meta = {
        'collection': 'course',  # Match MongoDB collection name
        'indexes': ['title', 'instructor'],
        'ordering': ['-created_at']
    }
