# firebase_fastAPI 🚀
## API rest con FastAPI(Python) a Firestore de Firebase(google) 🌎

### Primero instalaras las dependencias necesarias 🖥
```
pip install -r requirement.txt
```

### Para el uso de esta api rest, debera descargar las credenciales de firebase desde su consola de Firebase 🤓
Para realizar este proceso:
- Ingresa a [Firebase](https://console.firebase.google.com/) 🌎
- Crea un nuevo proyecto 🚀
- En el proyecto selecciona > Configuracion del proyecto > Cuentas de servicio > python 🐍
- Selecciona "Crear nueva clave privada" 🔑
- Agrega el archivo creado a la raiz del API REST 📩
- Renombra el archivo "serviceAccountKey.json" 📄

con esto ya podras correr tu API REST con el comando 🖥
```
uvicorn main:app --reload 
```
## End-points

la ruta http://127.0.0.1:8000/docs nos renderizara la documentacion interactiva de FastAPI, donde podremos probar los       endpoints que fuesemos a crear, y los que ya fueron agregados por defecto

la ruta http://127.0.0.1:8000/addUser podremos agregar usuarios por metodo POST 
  la estructura de datos del usuarios esta definida en el archivo 'models.py' en la raiz del API

la rura http://127.0.0.1:8000/ nos traera de vuelta la lista completa de usuarios que tengamos registrados 
  
Esta esta integracion entre plataformas fue realizada por @rtobart, autor de este repositorio 



Este template pertenece a @rtobart
