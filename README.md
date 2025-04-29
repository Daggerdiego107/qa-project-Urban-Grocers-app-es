# Automatización de Pruebas API: Sprint 7

Este proyecto realiza pruebas automáticas sobre un servicio REST para la creación de usuarios y kits.

##  Estructura de archivos

##### `configuration.py`
Define las URLs y rutas de los endpoints de la API.

##### `data.py`
Contiene los cuerpos (body) de las solicitudes y los encabezados (headers) necesarios para interactuar con la API.

##### `sender_stand_request.py`
Implementa funciones para enviar solicitudes HTTP (POST) para crear usuarios y kits.

##### `create_kit_name_kit_test.py`
Contiene las pruebas unitarias para validar el comportamiento esperado del endpoint de creación de kits.

##  Instalación

1. Asegúrate de tener **Python 3.11** o superior instalado.

2. Instala las librerías `requests` y `pytest` si no las tienes:

```
pip install requests
pip install pytest
```

Clona este proyecto o descarga los archivos.

## Descripción de Funciones

### 1. Crear un Usuario
- **Función:** `post_new_user(body)`
- **Ruta:** `POST /api/v1/users`
- **Encabezados requeridos:**
  - `"Content-Type" : "application/json"`
- **Cuerpo de Solicitud:**
  - `"firstName"`, `"phone"`, `"address"`

### 2. Crear un Kit
- **Función:** `post_new_kits(body)`
- **Ruta:** `POST /api/v1/kits`
- **Encabezados requeridos:**
  - `"Content-Type" : "application/json"`
  - `"Authorization" : "Bearer <authToken>"`
- **Cuerpo de Solicitud:**
  - `"name"`

##  Descripción de Pruebas

Las pruebas automáticas están en `create_kit_name_kit_test.py`.

### Pruebas Positivas

| # | Descripción |
|:--:|:------------|
| 1 | Crear kit con nombre de 1 carácter. |
| 2 | Crear kit con nombre de 511 caracteres. |
| 5 | Crear kit con caracteres especiales ("№%@,"). |
| 6 | Crear kit con espacios ("A Aaa"). |
| 7 | Crear kit con números ("123"). |

### Pruebas Negativas

| # | Descripción |
|:--:|:------------|
| 3 | Crear kit con nombre vacío — debe devolver error. |
| 4 | Crear kit con 512 caracteres — debe devolver error. |
| 8 | Enviar cuerpo de kit vacío — debe devolver error. |
| 9 | Enviar cuerpo de kit con número — debe devolver error. |

##  Ejecución de Pruebas

Puedes correr las pruebas ejecutando directamente el archivo de tests con `pytest`:

```
pytest create_kit_name_kit_test.py
```

## Notas importantes

- El valor del token de autorización (`Authorization`) en `data.py` debe estar actualizado y ser válido.
- Los nombres de kits deben cumplir las reglas del backend:
  - De 2 a 15 caracteres.
  - Solo letras latinas, espacios y guiones.


## Tecnologías utilizadas

- **Python 3.11**
- **Requests** : Para realizar solicitudes HTTP
- **Pytest** : Para manejo de tests más estructurado


## Autor

-Desarrollado por: Diego Antonio Navarro Ramirez
