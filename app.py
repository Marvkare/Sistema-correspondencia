import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import secrets

# Import the Blueprint from your new file
from blueprints.oficios import oficios_bp
from blueprints.usuarios import usuarios_bp

# Import the User and users dictionary from the new models file
from models import users, User

# Inicialización de la aplicación
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# Register the Blueprints with your app
app.register_blueprint(oficios_bp)
app.register_blueprint(usuarios_bp)

@login_manager.user_loader
def load_user(user_id):
    return users.get(int(user_id))

# --- Rutas de la aplicación ---
@app.route('/')
def index():
    return '<h1>Bienvenido. Para acceder, inicia sesión.</h1><a href="/login">Ir a login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = next((u for u in users.values() if u.username == username), None)

        if user and user.password == password:  # ¡IMPORTANTE! En producción, usarías un hash
            login_user(user)
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')
            return render_template('login.html')
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión correctamente.', 'info')
    return redirect(url_for('login'))

@app.route('/admin')
@login_required
def admin_panel():
    # Verifica si el usuario actual tiene el rol de administrador
    if 'admin_role' in current_user.roles:
        return '<h1>Panel de administración</h1><p>Funcionalidades de administrador aquí.</p>'
    else:
        flash('No tienes permisos para acceder a esta página.', 'warning')
        return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
