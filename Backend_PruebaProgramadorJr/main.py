

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configura el middleware CORS para permitir solicitudes de tu frontend Angular
origins = [
    "http://localhost:4200",  
    "https://localhost:8080",  
]

# Agrega el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permite los orígenes configurados
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)



app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(router)



@app.get("/")
def read_root():
    return {"message": "¡Holaaaaaaaaa esta funcionando!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

