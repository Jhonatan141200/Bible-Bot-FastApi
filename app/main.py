from fastapi import FastAPI, Query
import logging
import uvicorn
from model.model import get_model
from data.extract_json import get_context, custom_answer
from fastapi.middleware.cors import CORSMiddleware

# Importamos nuestro modleo BERT
model = get_model()

#Definimos un Log en Debug para control de errores
logging.basicConfig(level=logging.DEBUG)


# Metodo para repsonder  auna pregunta a aprtir de un contexto 
def get_result(qa, context, question, max_size=512):
    r = qa(context=context, question=question)
    return r


# Creamos una instancia de Fast API
app = FastAPI(title="Bible Bot Web Api",
              description=''' El objetivo es encontrar la repuesta correcta a 
              una pregunta dada por el usuario''',
              version="0.1.0",
              )

# Permitimos acceso a los métodos
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir cualquier origen
    allow_methods=["POST"],  # Permitir solo el método POST
    allow_headers=["*"],  # Permitir cualquier cabecera
)

# -----------METODOS A EXPONER WEB API -----------------
@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}

#Exponemos el servicio en un metodo POST
@app.post("/qas/")
async def get_qas(question: str = Query(..., min_length=3)):
    logging.debug("ejecutar modelo...")
    if question:
        context = get_context(question)
        if context:
            result = get_result(model, context, question)
            logging.debug("modelo ejecutado...")
            return {"respuesta": result["answer"]}
        else:
            return {"respuesta": custom_answer(question)}

# Activar solo para pruebas en local
"""
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8008)
"""