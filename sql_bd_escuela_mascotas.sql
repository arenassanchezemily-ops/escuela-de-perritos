-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS `escuela_mascotas` 
DEFAULT CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

USE `escuela_mascotas`;

-- 1. Tabla de Clientes (Dueños)
CREATE TABLE IF NOT EXISTS `clientes` (
  `id_cliente` INT AUTO_INCREMENT PRIMARY KEY,
  `nombre` VARCHAR(100) NOT NULL,
  `telefono` VARCHAR(20) NOT NULL,
  `email` VARCHAR(100) UNIQUE DEFAULT NULL,
  `fecha_registro` DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 2. Tabla de Mascotas
CREATE TABLE IF NOT EXISTS `mascotas` (
  `id_mascota` INT AUTO_INCREMENT PRIMARY KEY,
  `id_cliente` INT NOT NULL,
  `nombre` VARCHAR(50) NOT NULL,
  `especie` VARCHAR(30) NOT NULL DEFAULT 'Perro',
  `raza` VARCHAR(50) DEFAULT NULL,
  `fecha_nacimiento` DATE DEFAULT NULL,
  CONSTRAINT `fk_mascotas_clientes` 
    FOREIGN KEY (`id_cliente`) 
    REFERENCES `clientes` (`id_cliente`) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 3. Tabla de Inscripciones / Cursos
CREATE TABLE IF NOT EXISTS `inscripciones` (
  `id_inscripcion` INT AUTO_INCREMENT PRIMARY KEY,
  `id_mascota` INT NOT NULL,
  `curso` VARCHAR(100) NOT NULL,
  `fecha_inicio` DATE NOT NULL,
  `estado` ENUM('Activo', 'Completado', 'Cancelado') DEFAULT 'Activo',
  `notas` TEXT DEFAULT NULL,
  CONSTRAINT `fk_inscripciones_mascotas` 
    FOREIGN KEY (`id_mascota`) 
    REFERENCES `mascotas` (`id_mascota`) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insertar datos de prueba opcionales
INSERT INTO `clientes` (`nombre`, `telefono`, `email`) VALUES
('María López', '+56912345678', 'maria@example.com'),
('Carlos Gómez', '+56987654321', 'carlos@example.com');

INSERT INTO `mascotas` (`id_cliente`, `nombre`, `especie`, `raza`) VALUES
(1, 'Max', 'Perro', 'Golden Retriever'),
(2, 'Luna', 'Perro', 'Pastor Alemán');

INSERT INTO `inscripciones` (`id_mascota`, `curso`, `fecha_inicio`, `estado`) VALUES
(1, 'Obediencia Básica', CURRENT_DATE(), 'Activo'),
(2, 'Socialización de Cachorros', CURRENT_DATE(), 'Activo');