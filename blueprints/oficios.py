# blueprints/oficios.py

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

# Create a Blueprint named 'oficios'
oficios_bp = Blueprint('oficios', __name__, url_prefix='/oficios')

# Route for listing all oficios
@oficios_bp.route('/')
@login_required
def list_oficios():
    # Logic to fetch and display the list of oficios
    return render_template('oficios/list.html')

# Route for creating a new oficio
@oficios_bp.route('/new', methods=['GET', 'POST'])
@login_required
def new_oficio():
    if request.method == 'POST':
        # Logic to save the new oficio to the database
        # ...
        return redirect(url_for('oficios.list_oficios'))
    
    return render_template('oficios/new.html')

# Route for viewing a single oficio
@oficios_bp.route('/<int:oficio_id>')
@login_required
def view_oficio(oficio_id):
    # Logic to fetch a specific oficio by its ID
    return f"<h1>Viewing Oficio ID: {oficio_id}</h1>"