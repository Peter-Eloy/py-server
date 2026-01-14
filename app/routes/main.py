from flask import Blueprint, jsonify, redirect, url_for

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return redirect(url_for('admin.index'))

@main_bp.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        'name': 'Flask API',
        'version': '1.0',
        'description': 'A simple Flask API example'
    })