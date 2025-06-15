# Documentación

**Proyecto: Manejo de Cursos Virtuales**

Este documento describe cómo ejecutar, probar y entender la arquitectura de la aplicación de gestión de cursos virtuales.

---

## 📦 1. Ejecución en Producción

Instrucciones para levantar todos los servicios en modo producción:

```bash
docker compose -f docker-compose.prod.yml up --build
```

Accede a:

- Frontend: `http://localhost:4000/`
- Backend API: `http://localhost:4000/back/`
- Documentación OpenAPI/Swagger: `http://localhost:4000/back/docs/`

Para detener y limpiar:

```bash
docker compose -f docker-compose.prod.yml down --volumes --remove-orphans
```

---

## 🛠️ 2. Ejecución en Desarrollo

Levanta todos los servicios (base, migraciones, API, frontend) usando perfiles:

```bash
docker compose -f docker-compose.dev.yml --profile run up --build
```

Accede a:

- Frontend de desarrollo: `http://localhost:5173/`
- Backend de desarrollo: `http://localhost:8000/`
- Documentación local de FastAPI: `http://localhost:8000/docs/`

Para detener y limpiar volúmenes:

```bash
docker compose -f docker-compose.dev.yml --profile run down -v --remove-orphans
```

---

## 🚨 3. Ejecución de Tests y Snapshot Updates

### Back-end

```bash
# Ejecutar tests de backend
docker compose -f docker-compose.dev.yml --profile test up --build back_test

# Actualizar snapshots de backend (cuando cambias lógica)
docker compose -f docker-compose.dev.yml --profile test up --build back_update_snap
```

### Front-end

```bash
# Ejecutar tests de frontend
docker compose -f docker-compose.dev.yml --profile test up --build front_test

# Actualizar snapshots de frontend
docker compose -f docker-compose.dev.yml --profile test up --build front_update_snap
```

> ¿Por qué snapshots?
> 
> 
> La estrategia de *snapshot testing* captura el estado esperado de componentes o vistas, facilitando la detección de cambios inadvertidos y asegurando regresiones controladas. Al actualizar snapshots, redefinimos la "fuente de la verdad" tras cambios intencionados.
> 

---

## 📐 4. Herramientas y Decisiones Técnicas

### Estructura del Proyecto

- **`back/`**: Código de FastAPI (Python) con SQLAlchemy + Alembic para migraciones.
- **`front/`**: Proyecto en React, con Vite y  TailwindCSS.
- **`database/`**: Scripts y volúmenes para entornos dev y prod.
- **`nginx/`**: Reverse proxy para producción, unifica front, back y documentación bajo un mismo dominio.

###

### Backend

- **Framework**: *FastAPI*, por su generación automática de documentación y rendimiento.
- **Migraciones**: *Alembic*, transforma modelos de SQLAlchemy a esquemas de BD.
- **ORM**: *SQLAlchemy*, con patrón *Factory* para abstracción de operaciones CRUD y serialización.
- **Validación**: *Pydantic*, esquemas para validar requests entrantes.
- **Dependencias**: *Pipenv* para aislar y pinear dependencias.
- **Testing**: *pytest* + *snapshottest*, facilita pruebas reproducibles y verificación de salidas complejas.
- **Autogeneración de modelos**: *sqlacodegen* acelera la creación de esquemas desde bases ya existentes.

### Frontend

- **Gestión de formularios**: *React Hook Form* + *Zod* , permite validación declarativa y robusta del lado del cliente.
- **Estilos**: *Tailwind CSS*, diseño responsivo y mantenible sin hojas de estilo adicionales.
- **Testing**: *Vitest* + *Testing Library* + *MSW* para pruebas unitarias e integración controladas, aislando llamadas a red con mocks.

### Contenedores y Redes

- **Docker Compose** con perfiles (`run`, `test`) para controlar servicios por contexto.
- **Nginx** como *reverse proxy* en producción evita errores CORS y facilita la integración de futuros servicios (monitorización, métricas, etc.) bajo el mismo dominio.