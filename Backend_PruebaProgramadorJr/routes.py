from fastapi import APIRouter
from controller import ArticuloController
from models import Articulo

router = APIRouter(prefix="/articulo",tags=['articulo'],responses={404:{"detail":"ruta no encontrada"}})


@router.post("/create",response_model=Articulo,status_code=201)
async def Create(element:Articulo):
    return ArticuloController.Create(element)

@router.get("/read")
async def Read():
    return ArticuloController.Read()

@router.get("/readbysku")
async def Read(sku:str):
    return ArticuloController.ReadArticuloBySku(sku)


@router.put("/update",response_model=Articulo,status_code=201)
async def Update(element:Articulo):
    return ArticuloController.Update(element)


@router.delete("/delete/{codigo}")
async def Delete(codigo:int):
    return ArticuloController.Delete(codigo)

