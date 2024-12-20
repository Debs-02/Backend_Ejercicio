# Backend_Ejercicio

Este es el backend de un proyecto de gestión de artículos, construido con **FastAPI**.

## Requisitos previos
Antes de ejecutar el backend, asegúrate de tener instalados los siguientes programas:
- [Python 3.x](https://www.python.org/downloads/): Es necesario para ejecutar el proyecto.

### Instalación

1. **Clonar el repositorio del proyecto**:
   ```bash
     git clone <URL del repositorio>
     cd <directorio del repositorio>
2.Instalar  dependencias: Una vez que hayas clonado el repositorio, es necesario instalar las siguientes dependencias:
  -Pyodbc: pip install pyodbc ó python3 -m pip install pyodbc
  -FastApi: pip install fastapi
  -Uvicorn: pip install uvicorn[standard[

3-Ejecutar el servidor:
  python3 -m uvicorn main:app --reload --port 8080
  Esto iniciará el servidor en http://localhost:8080.

4-Verificación:
Abre tu navegador y ve a la siguiente URL para probar la API:
http://localhost:8080/docs: Interfaz de documentación automática de FastAPI.
