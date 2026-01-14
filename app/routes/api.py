from flask import Blueprint, jsonify, send_file, request
from app.models import Project, Endpoint
import os

api_bp = Blueprint('api', __name__)

@api_bp.route('/<project_name>/<path:endpoint_path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def dynamic_endpoint(project_name, endpoint_path):
    # Find project
    project = Project.query.filter_by(name=project_name).first_or_404()
    
    # Find endpoint matching path and method
    endpoint = Endpoint.query.filter_by(
        project_id=project.id,
        path=f"/{endpoint_path}",
        method=request.method
    ).first_or_404()
    
    # Return file response
    if endpoint.response_type == 'file' and endpoint.file_path:
        if os.path.exists(endpoint.file_path):
            return send_file(endpoint.file_path)
        return jsonify({'error': 'File not found'}), 404
    
    # Return JSON response
    return jsonify(endpoint.get_response_data())