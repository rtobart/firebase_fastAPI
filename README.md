# firebase_fastAPI 🚀
## API rest con FastAPI(Python) a Firestore de Firebase(google) 🌎

### Primero instalaras las dependencias necesarias 🖥
```
pip install -r requirement.txt
```

### Para el uso de esta api rest, debera descargar las credenciales de firebase desde su consola de Firebase 🤓
Para realizar este proceso:
- Ingresa a https://console.firebase.google.com/ 🌎
- Crea un nuevo proyecto 🚀
- En el proyecto selecciona > Configuracion del proyecto > Cuentas de servicio > python 🐍
- Selecciona "Crear nueva clave privada" 🔑
- Agrega el archivo creado a la raiz del proyecto 📩
- Renombra el archivo "serviceAccountKey.json" 📄

con esto ya podras correr tu API REST con el comando 🖥
```
uvicorn main:app --reload 
```

Este template pertenece a @rtobart
