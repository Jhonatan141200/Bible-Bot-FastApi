import requests
import json
from difflib import SequenceMatcher as SM

# Extraemos el contexto de nuestro archivo JSON para sr procesador por nuestro modelo
def get_context(question):
    url = 'https://base-datos-bible-1997.netlify.app/'
    response = requests.get(url)
    content = response.content.decode('utf-8')
    datos = json.loads(content, strict=False)
    context = ''
    for data in (datos['data']):
        flag = False;
        for frase in data['palabras_clave']:
            if (SM(None, frase, question).ratio() > 0.85):
                flag = True
        if flag:
            context = data['parrafo'][0]['context']
            break
    return context



def custom_answer(question):
    greeting = {
        "Hola": "Hola soy Bible Bot, ¡ Estoy listo para ayudarte!",
        "Adiós": "Cuidate, sigue estudiando la biblia !",
        "Nos vemos": "Hasta pronto !!",
    }
    result = "Disculpa, No entendí la pregunta, ¿Podrías repetirla?"
    for q, c in greeting.items():
        if (SM(None, q, question).ratio() > 0.75):
            result = c
    return result        
            

    
    
    
    



