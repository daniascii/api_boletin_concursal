import requests
from bs4 import BeautifulSoup

# Se crea una sesion para manejar las cookies y el CSRF token
session = requests.Session()

# Se obtienen los datos de la pagina inicial para obtener el CSRF token
url_inicio = "https://www.boletinconcursal.cl/boletin"
respuesta = session.get(url_inicio)

# Se parsea el HTML para obtener el CSRF token
soup = BeautifulSoup(respuesta.text, "html.parser")
csrf_token = soup.find("input", {"name": "_csrf"})["value"]

# Se establecen los datos para conectarse a la API
url_api = "https://www.boletinconcursal.cl/boletin/getRegistroDiarioPublicacionJson"
payload = {
    "_csrf": csrf_token,
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Se conecta a la API y se obtiene el JSON con los datos del boletín concursal
respuesta_post = session.post(url_api, data=payload, headers=headers)

datos = respuesta_post.json() # formato {tribunal,rolCasusa,tipoProcedimiento,deudorNombre,rut,entePublicador,nombrePublicacion,fechaPublicacion}
# para hacer lo que quieras con los datos resultantes