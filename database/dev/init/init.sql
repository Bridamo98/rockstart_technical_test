-- Instructors table
CREATE TABLE IF NOT EXISTS instructors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    bio TEXT NOT NULL
);

-- Instructors inserts
INSERT INTO instructors (name, email, bio) VALUES
('Ana Martínez', 'ana.martinez@example.com', 'Especialista en matemáticas aplicadas y educación online.'),
('Carlos Gómez', 'carlos.gomez@example.com', 'Ingeniero de software con experiencia en desarrollo web y móvil.'),
('Lucía Fernández', 'lucia.fernandez@example.com', 'Doctora en física y apasionada por la enseñanza.'),
('Pedro Ramírez', 'pedro.ramirez@example.com', 'Experto en inteligencia artificial y machine learning.'),
('María López', 'maria.lopez@example.com', 'Profesora de química con más de 10 años de experiencia.'),
('Javier Torres', 'javier.torres@example.com', 'Desarrollador backend y entusiasta de bases de datos.');

-- Courses table
CREATE TABLE IF NOT EXISTS courses (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    course_desc TEXT NOT NULL,
    instructor_id INTEGER NOT NULL,
    CONSTRAINT fk_courses_instructor_id FOREIGN KEY (instructor_id)
        REFERENCES instructors (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Courses inserts
INSERT INTO courses (title, course_desc, instructor_id) VALUES
('Matemáticas Básicas', 'Curso introductorio a las matemáticas básicas.', 1),
('Desarrollo Web', 'Aprende a crear sitios web modernos.', 2),
('Física Avanzada', 'Explora conceptos avanzados de física.', 3),
('Inteligencia Artificial', 'Introducción a los conceptos y aplicaciones de IA.', 4),
('Química General', 'Fundamentos de la química para principiantes.', 5),
('Bases de Datos', 'Aprende sobre diseño y gestión de bases de datos.', 6),
('Machine Learning', 'Curso práctico de aprendizaje automático.', 4),
('Química Orgánica', 'Estudio de compuestos orgánicos y sus reacciones.', 5);


-- Lesson Table
CREATE TABLE IF NOT EXISTS lessons (
    id SERIAL PRIMARY KEY,
    course_id INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    video_url TEXT NOT NULL,
    CONSTRAINT fk_lessons_course_id FOREIGN KEY (course_id)
        REFERENCES public.courses (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Lessons inserts
INSERT INTO lessons (course_id, title, video_url) VALUES
(1, 'Introducción a las Matemáticas', 'https://www.youtube.com/watch?v=-RDBMu7BreE&pp=ygUaaW50cm9kdWNjaW9uIGEgbWF0ZW1hdGljYXM%3D'),
(1, 'Álgebra Básica', 'https://www.youtube.com/watch?v=_6uyQISZvBc&pp=ygUOYWxnZWJyYSBiYXNpY2E%3D'),
(2, 'HTML y CSS', 'https://www.youtube.com/watch?v=ELSm-G201Ls&pp=ygUKaHRtbCB5IGNzcw%3D%3D'),
(2, 'JavaScript Básico', 'https://www.youtube.com/watch?v=QoC4RxNIs5M&pp=ygUSSmF2YVNjcmlwdCBCw6FzaWNv'),
(3, 'Mecánica Clásica', 'https://www.youtube.com/watch?v=psms00DeX9o&pp=ygUYbWVjw6FuaWNhIGNsw6FzaWNhIGN1cnNv'),
(3, 'Electromagnetismo', 'https://www.youtube.com/watch?v=cFaf1_P2Y8c&pp=ygUXRWxlY3Ryb21hZ25ldGlzbW8gY3Vyc28%3D'),
(4, 'Introducción a la IA', 'https://www.youtube.com/watch?v=CjdusCm73p0&pp=ygUVSW50cm9kdWNjacOzbiBhIGxhIElB'),
(4, 'Redes Neuronales', 'https://www.youtube.com/watch?v=jKCQsndqEGQ&pp=ygUWUmVkZXMgTmV1cm9uYWxlcyBjdXJzbw%3D%3D'),
(5, 'Estructura Atómica', 'https://www.youtube.com/watch?v=Xvno5NeanxU&pp=ygUZRXN0cnVjdHVyYSBBdMOzbWljYSBjdXJzbw%3D%3D'),
(5, 'Reacciones Químicas', 'https://www.youtube.com/watch?v=smlrUR_UXnk&pp=ygUaUmVhY2Npb25lcyBRdcOtbWljYXMgY3Vyc28%3D'),
(6, 'Modelado de Datos', 'https://www.youtube.com/watch?v=aFgHVE_Y_YU&pp=ygUXTW9kZWxhZG8gZGUgRGF0b3MgY3Vyc28%3D'),
(6, 'SQL Básico', 'https://www.youtube.com/watch?v=OuJerKzV5T0&pp=ygURU1FMIELDoXNpY28gY3Vyc2_SBwkJ3gkBhyohjO8%3D'),
(7, 'Regresión Lineal', 'https://www.youtube.com/watch?v=k964_uNn3l0&t=141s&pp=ygUaUmVncmVzacOzbiBMaW5lYWwgY3Vyc28gSUHSBwkJ3gkBhyohjO8%3D'),
(7, 'Clasificación', 'https://www.youtube.com/watch?v=8-nt3Urok4E&pp=ygUkQ2xhc2lmaWNhY2lvbiBtYWNoaW5lIGxlYXJuaW5nIGN1cnNv0gcJCd4JAYcqIYzv'),
(8, 'Hidrocarburos', 'https://www.youtube.com/watch?v=itVIgu2WAU8&pp=ygUTSGlkcm9jYXJidXJvcyBjdXJzbw%3D%3Ds'),
(8, 'Reacciones Orgánicas', 'https://www.youtube.com/watch?v=gdHecHHkj38&pp=ygUbUmVhY2Npb25lcyBPcmfDoW5pY2FzIGN1cnNv');
