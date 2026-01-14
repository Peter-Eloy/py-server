from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(500))
    endpoints = db.relationship('Endpoint', backref='project', lazy=True, cascade='all, delete-orphan')

class Endpoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    path = db.Column(db.String(200), nullable=False)  # e.g., "/users"
    method = db.Column(db.String(10), nullable=False)  # GET, POST, etc.
    response_type = db.Column(db.String(20), default='json')  # 'json' or 'file'
    
    # For JSON responses
    response_body = db.Column(db.Text)  # Store JSON as text
    
    # For file responses (PDFs, etc.)
    file_path = db.Column(db.String(500))  # Local file path
    
    def get_response_data(self):
        """Parse JSON response body"""
        if self.response_body:
            return json.loads(self.response_body)
        return {}