from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, Project, Endpoint

admin_bp = Blueprint('admin', __name__)

# List all projects
@admin_bp.route('/')
def index():
    projects = Project.query.all()
    return render_template('admin/projects.html', projects=projects)

# Create new project
@admin_bp.route('/project/new', methods=['GET', 'POST'])
def new_project():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form.get('description', '')
        
        project = Project(name=name, description=description)
        db.session.add(project)
        db.session.commit()
        
        return redirect(url_for('admin.index'))
    
    return render_template('admin/project_form.html')

# View project endpoints
@admin_bp.route('/project/<int:project_id>')
def view_project(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('admin/endpoints.html', project=project)

# Create new endpoint
@admin_bp.route('/project/<int:project_id>/endpoint/new', methods=['GET', 'POST'])
def new_endpoint(project_id):
    project = Project.query.get_or_404(project_id)
    
    if request.method == 'POST':
        endpoint = Endpoint(
            project_id=project_id,
            path=request.form['path'],
            method=request.form['method'],
            response_type=request.form['response_type'],
            response_body=request.form.get('response_body', ''),
            file_path=request.form.get('file_path', '')
        )
        db.session.add(endpoint)
        db.session.commit()
        
        return redirect(url_for('admin.view_project', project_id=project_id))
    
    return render_template('admin/endpoint_form.html', project=project)

# Delete endpoint
@admin_bp.route('/endpoint/<int:endpoint_id>/delete', methods=['POST'])
def delete_endpoint(endpoint_id):
    endpoint = Endpoint.query.get_or_404(endpoint_id)
    project_id = endpoint.project_id
    db.session.delete(endpoint)
    db.session.commit()
    return redirect(url_for('admin.view_project', project_id=project_id))