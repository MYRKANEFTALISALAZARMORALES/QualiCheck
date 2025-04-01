# Importación de FastAPI
from fastapi import FastAPI

# Importación de los enrutadores de los distintos módulos
from app.api.endpoints import inspections, defects, users, notifications

# Creación de la instancia de la aplicación FastAPI
app = FastAPI(title="QualiCheck API")

# Inclusión del enrutador de inspecciones
app.include_router(inspections.router, prefix="/inspections", tags=["Inspections"])

# Inclusión del enrutador de defectos
app.include_router(defects.router, prefix="/defects", tags=["Defects"])

# Inclusión del enrutador de usuarios
app.include_router(users.router, prefix="/users", tags=["Users"])

# Inclusión del enrutador de notificaciones
app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])

# Definición de la ruta raíz
@app.get("/")
def read_root():
    """
    Endpoint raíz que devuelve un mensaje de confirmación de que la API está en ejecución.
    
    Retorna:
        dict: Mensaje de estado de la API.
    """
    return {"message": "QualiCheck API is running"}