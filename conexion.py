import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# creamos la variable Credencial=>(cred) y le cargamos el archivo credencial de firebase
cred = credentials.Certificate("serviceAccountKey.json")
# instanceamos la firebase con las credenciales
firebase_admin.initialize_app(cred)
# creamos una instancia de FireStore que sera nuestra base de datos=>(db)
db = firestore.client()
# esta variable instancia de la base de datos la importaremos en el archivo main!!!