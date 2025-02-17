from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
import uuid

api = FastAPI(
    title="MLOPS Trabajo Practico 2",
    description="MLOPS Trabajo Practico 2",
    version="0.0.1",
)

usuarios = []  # Aquí almacenaremos los usuarios

@api.post("/usuarios/", tags=["Usuarios"])
async def user_sign_up(data: dict):
    id_usuario = str(uuid.uuid4())
    user = {
        "id": id_usuario,
        "name": data["name"],
        "email": data["email"],
        "username": data["username"]
    }
    usuarios.append(user)
    return {
        "response": f"Se ha creado exitosamente el usuario {data['username']} con el email {data['email']}",
        "id": id_usuario,
        "name": data["name"],
    }
