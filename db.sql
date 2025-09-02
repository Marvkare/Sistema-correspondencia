"Datos del oficio"
fecha -
mes -
folio -
persona u organizacion  -
domicilio  - Persona o orgnizacion
telefono - El telefono es de la persona u organizacion ? 
no oficio -
peticion-
Area 
estatus --> entregdo atendido pendiente  no atendido 
folio de respuesta y seguimiento - 
observaciones --> observaciones del por que 
areas = lugares a los que se llevan oficios 


"Formato diario"

FECHA 
MES 
FOLIO 
PERSONA U ORGANIZACION 
DOMICILIO 
TELEFONO 
No. OFICIO
PETICION
DIRECCION DE  TURNO 
ESTATUS 
OBSERVACIONES  

"area responsable y area obserbable 

tiene pdf con el numero de oficio"




CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(50) NOT NULL UNIQUE,
    contrasena_hash VARCHAR(255) NOT NULL,
    nombre_completo VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE roles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_rol VARCHAR(50) NOT NULL UNIQUE,
    descripcion TEXT
);

CREATE TABLE usuario_roles (
    usuario_id INT,
    rol_id INT,
    PRIMARY KEY (usuario_id, rol_id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (rol_id) REFERENCES roles(id) ON DELETE CASCADE
);

CREATE TABLE oficios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE,
    mes VARCHAR(20),
    folio VARCHAR(50),
    no_oficio VARCHAR(50),
    persona_u_organizacion VARCHAR(255),
    domicilio VARCHAR(255),
    telefono VARCHAR(50),
    peticion TEXT,
    area VARCHAR(100),
    estatus VARCHAR(50),
    folio_respuesta_seguimiento VARCHAR(50),
    observaciones TEXT,
    direccion_de_turno VARCHAR(100),
    pdf_oficio_url VARCHAR(255)
);


CREATE TABLE activity_log (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    action VARCHAR(255) NOT NULL,
    resource VARCHAR(255) NOT NULL,
    resource_id INT,
    timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    details TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
