from conexion import db
from fastapi import FastAPI
from models import User

# llamamos a la coleccion users de la db(instancia de firestore)
users = db.collection(u'users')

# creamos una instancia de FastAPI para tener acceso a las rutas 
app = FastAPI()

# definimos el comportamiento de la ruta http://127.0.0.1:8000/ con metodo GET
@app.get("/")
async def root():
    # con users.get() que pertenece a firebase, traemos todos los usuarios de la lista
    usersRef = users.get()
    # creamo un diccionario para retornarlo como json
    usersJson = {}
    # recorremos la lista de usuarios
    for user in usersRef:
        # agregamos cada usuario recuperado al diccionario
        usersJson[user.id] = user.to_dict()
    # Retornamos el diccionario
    return usersJson

# definimos el comportamiento de la ruta http://127.0.0.1:8000/addUser con metodo POST
@app.post("/addUser")
async def addUser(user: User): #pasamos por parametro el modelo de usuario {name, lastName, born}
    # creamos una instancia de la lista de usuarios y añadimos el id como llave del diccionario
    userAdd = users.document(f'{user.id}') 
    # agregamos los parametros internos del diccionario y enviamos los cambios
    userAdd.set({
        # a la izquierda vemos el nombre del campo en la base de datos
        u'nombre': user.name, # a la derecha vemos el dato que le pasamos por parametro del POST
        u'apellido': user.lastName,
        u'nacimiento': user.born
    })
    return {'status' : 200} #retornamos una mensaje de exito



# definimos el comportamiento de la ruta http://127.0.0.1:8000/delUser con metodo DELETE
@app.delete("/delUser")
async def delUser(id): #pasamos por parametro id de usuario 
    # se elimina usuario en coleccion que posea id
    userRef=db.collection(u'users').document(id)
    user= userRef.get()
    if user.exists:        
        users.document(f'{id}').delete()      
    else:
        print(f'Usuario con id {id} no existe')    
    return {'status' : 200} #retornamos una mensaje de exito