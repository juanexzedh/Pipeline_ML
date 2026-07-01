import pandas as pd
from fastapi import FastAPI
import joblib, json, os
from .schema import SolicitudPrediccion
from fastapi.middleware.cors import CORSMiddleware

# Configuración de rutas (Rutas dinamicas)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Esto sube un nivel (..) desde 'api' para buscar la carpeta 'model'
MODEL_PATH = os.path.join(BASE_DIR, '..', 'model', 'modelo_calidad_aire_rf.pkl')
JSON_PATH = os.path.join(BASE_DIR, '..', 'model', 'columnas_modelo.json')

# Carga del Modelo y mapa de columnas
model = joblib.load(MODEL_PATH)
with open(JSON_PATH, "r") as f:
    columnas_modelo = json.load(f)

# Inicializacion de la aplicacion
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite peticiones desde cualquier origen en desarrollo
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

# Endpoint para verificar que la API está encendida
@app.get("/")
def home():
    return {"message": "API de Calidad del Aire activa"}

# Endpoint de Prediccion
@app.post("/predict")
def predict(data: SolicitudPrediccion):
    # Convertir los datos recibidos (que son un objeto Pydantic) a un DataFrame
    df = pd.DataFrame([data.model_dump()])
    
    # Aplicar get_dummies
    df_encoded = pd.get_dummies(df)
    
    # reindex con la lista que cargamos en 'columnas_modelo'
    # 'fill_value=0' es vital para que las columnas ausentes sean 0
    df_final = df_encoded.reindex(columns=columnas_modelo, fill_value=0)
    
    # El modelo espera una matriz
    resultado = model.predict(df_final)
    
    # Retornar el resultado
    # Nota: model.predict devuelve un array, asi que se extrae el primer valor
    return {"prediccion": float(resultado[0])}

    #para inicializar: python -m uvicorn api.main:app --reload