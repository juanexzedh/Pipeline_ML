from pydantic import BaseModel, Field

class SolicitudPrediccion(BaseModel):
    # Variables Geográficas
    Nombre_del_Departamento: str = Field(..., example="BOGOTÁ, D.C.")
    Nombre_del_Municipio: str = Field(..., example="BOGOTÁ, D.C.")
    Latitud: float = Field(..., example=4.65)
    Longitud: float = Field(..., example=-74.10)
    
    # Variables de Configuración de la Estación
    Variable: str = Field(..., example="PM10") # El tipo de contaminante
    Tipo_de_Estacion: str = Field(..., example="Fija")
    Ubicacion: str = Field(..., example="Urbana")
    
    # Variables Temporales
    Año: str = Field(..., example="2026") # Se asume tipo 'str' según el info() de pandas
    Tiempo_de_exposicion_horas: int = Field(..., example=24)