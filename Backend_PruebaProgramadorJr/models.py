from pydantic import BaseModel,field_validator
from datetime import datetime
class Articulo(BaseModel):
   Codigo:int
   sku:str
   nombre:str
   marca:str
   cantidad:int
   fecha_creacion:str




