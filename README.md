# firebase_fastAPI 🚀
Antes de partir te recomiendo que trabajes con entornos virtuales como:
- [VENV](https://docs.python.org/3/library/venv.html)
## API rest con FastAPI(Python) a Firestore de Firebase(google) 🌎
```
git clone https://github.com/rtobart/firebase_fastAPI.git
```

### Primero instalaras las dependencias necesarias 🖥
```
pip install -r requirement.txt
```

### Para el uso de esta api rest, debera descargar las credenciales de firebase desde su consola de Firebase 🤓
Para realizar este proceso:

- Ingresa a [Firebase](https://console.firebase.google.com/) 🌎
- Crea un nuevo proyecto 🚀
- Crea firestore database en modo produccion o pruebas
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

la ruta http://127.0.0.1:8000/ nos traera de vuelta la lista completa de usuarios que tengamos registrados 

la ruta http://127.0.0.1:8000/delUser podemos eliminar usuarios por metodo DELETE
  requiere id de usuario a eliminar

la ruta http://127.0.0.1:8000/modName podemos modificar el nombre del usuario Requiere id del usuario

Esta esta integracion entre plataformas fue realizada por [@rtobart](https://github.com/rtobart), autor de este repositorio

para mayor informacion revisa la documentacion oficial de estas tecnologias 
- [Firebase documentation](https://firebase.google.com/docs?authuser=0&hl=es)
- [FastAPI documentation](https://fastapi.tiangolo.com/tutorial/)

Este template pertenece a [@rtobart](https://github.com/rtobart)
