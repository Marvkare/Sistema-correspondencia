# blueprints/usuarios.py

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

# Simulación de la base de datos de usuarios y roles
# En una aplicación real, esto se manejaría con SQLAlchemy
from app import users, roles, User

usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

def is_admin():
    """Verifica si el usuario actual tiene el rol de administrador."""
    return 'admin_role' in current_user.roles

@usuarios_bp.before_request
@login_required
def check_admin_access():
    """Protege todas las rutas del blueprint, excepto el login, para que solo
    sean accesibles por administradores."""
    if not is_admin():
        flash('No tienes permisos para acceder a esta página.', 'danger')
        return redirect(url_for('main.dashboard'))

@usuarios_bp.route('/manage_users')
def manage_users():
    """Muestra la lista de usuarios y un formulario para crear nuevos."""
    return render_template('usuarios/manage.html', users=users.values())

@usuarios_bp.route('/manage_users/create', methods=['POST'])
def create_user():
    """Crea un nuevo usuario."""
    username = request.form['username']
    password = request.form['password'] # ¡Recuerda hashear en producción!
    
    # Asigna un ID simple para el ejemplo
    new_id = len(users) + 1
    users[new_id] = User(new_id, username, password)
    
    flash(f'Usuario "{username}" creado exitosamente.', 'success')
    return redirect(url_for('usuarios.manage_users'))

@usuarios_bp.route('/manage_users/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    """Elimina un usuario por su ID."""
    if user_id in users:
        del users[user_id]
        flash('Usuario eliminado exitosamente.', 'success')
    else:
        flash('El usuario no existe.', 'danger')
    return redirect(url_for('usuarios.manage_users'))