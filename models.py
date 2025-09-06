from flask_login import UserMixin

# --- Simulación de una base de datos de usuarios ---
# En un entorno real, usarías una base de datos como SQL con SQLAlchemy
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
        self.roles = [] # Aquí se almacenan los roles del usuario

# Usuario por defecto y "base de datos"
users = {
    1: User(1, 'admin', 'adminpassword')
}

roles = {
    'admin': ['admin_role'], # Ejemplo de rol
}

# Asigna el rol 'admin' al usuario 'admin'
users[1].roles.append('admin_role')
