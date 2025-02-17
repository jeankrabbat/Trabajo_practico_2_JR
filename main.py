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

@api.get("/usuarios/{user_id}", tags=["Usuarios"])
async def get_user(user_id: str):
    try:
        user = next((u for u in usuarios if u["id"] == user_id), None)
        if user is not None:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=user
            )
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "response": "No se ha podido encontrar el usuario",
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )