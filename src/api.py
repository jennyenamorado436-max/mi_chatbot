from fastapi import FastAPI
from pydantic import BaseModel
from src.inference import responder

app = FastAPI()

class Mensaje(BaseModel):
    texto: str

@app.post("/chat")
def chat(mensaje: Mensaje):
    respuesta = responder(mensaje.texto)
    return {"respuesta": respuesta}