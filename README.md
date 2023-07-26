# BIBLE BOT WEB API
Este proyecto Web Api expone un métdo post que recibe una pregunta como query params y gracias a un modelo NLP pre-entrenado es capaz de generar una repuesta de acuerdo a un contexto dado y devolver un texto en JSON como repuesta.

## Nota
El desarollo de esta app forma parte de nuestro proyecto titulado "IMPLEMENTACIÓN DE UN CHATBOOT QUE AYUDE AL ESTUDIO DE LA BIBLIA PARA LOS MIEMBROS DE IASD TRUJILLO - CENTRAL" y fue presentado como trabajo final en el curso de Taller Integrador en UPAO con el docente Walter Cueva.

[Derechos reservados Correa Cerna & Vasquez Reyna]

## Pasos para la ejecución
1. Librerias requeridas
   + FastApi 
   + Tranformers
   + Torch
   + Json
   + uvicorn
2. Descargar Modelo Bert
   + Entrar al enlace https://drive.google.com/drive/folders/1-Hi8TFPeqnpojGZugcxA__bCQkP6veeI?usp=sharing
   + Descargar toda la carpeta y ubicarla en el archivo raíz del proyecto
   + La estructura de carpetas final debe verse así

   ![image](https://github.com/Jhonatan141200/Bible-Bot-FastApi/assets/83673179/51af1004-9030-4bba-86a1-5faf7d94b6b6)

3. Ejecutar el archivo main.py
   
   ![image](https://github.com/Jhonatan141200/Bible-Bot-FastApi/assets/83673179/54405d74-f00b-4832-a4c8-5f933f43883d)

## UI del servicio WEB API
![image](https://github.com/Jhonatan141200/Bible-Bot-FastApi/assets/83673179/2e27e94f-26b7-4bec-864e-1f76bfaa8309)
