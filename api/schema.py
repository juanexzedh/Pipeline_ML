from pydantic import BaseModel, Field

class SolicitudPrediccion(BaseModel):

    #Se establecen las variables necesarias para la prediccion
    Variable: str = Field(..., example="PM10")
    Año: str = Field(..., example="2026")
    Nombre_del_Departamento: str = Field(..., example="ANTIOQUIA")
    Nombre_del_Municipio: str = Field(..., example="MEDELLÍN")
    Latitud: float = Field(..., example=6.2518)
    Longitud: float = Field(..., example=-75.5636)
    # Nota: 
    # Segun el listado de columnas original y la lista de eliminacion, 
    # variables como 'Unidades' o 'Tiempo de exposición (horas)' no fueron 
    # eliminadas explicitamente en el código compartido. 
    Unidades: str = Field(..., example="µg/m3")
    Tiempo_de_exposicion_horas: int = Field(..., example=24)