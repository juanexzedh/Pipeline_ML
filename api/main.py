from pydantic import BaseModel
import pandas as pd
import numpy as np
from fastapi import FastAPI
import joblib, schema

# 1. Carga del Modelo (Lo primero al ejecutar la api)
model = joblib.load("model/modelo_calidad_aire_rf.pkl")

# 2. Inicializacion de la aplicacion
app = FastAPI()

# Endpoint para verificar que la API está encendida
@app.get("/")
def home():
    return {"message": "API de Calidad del Aire activa"}

# Endpoint de Predicción
@app.post("/predict")
def predict(data: SolicitudPrediccion):
    # Aquí es donde ocurre la transformación.
    # Recibimos un objeto validado por Pydantic.
    # 1. Convertir 'data' a un formato que Pandas entienda.
    # 2. Aplicar el proceso de dummies y reindexar (nuestra lógica).
    # 3. Llamar a model.predict().
    # 4. Retornar el resultado.
    pass