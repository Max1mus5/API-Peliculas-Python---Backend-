# Fast-API 
Backend UTP Course

# Documentación de la Aplicación de Películas

Esta aplicación es un servidor de API construido con FastAPI que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en una base de datos de películas.

## Inicar Entorno Virtual
Para iniciar el entorno virtual en Windows, ejecuta el siguiente comando en la terminal:
```bash
venv/Scripts/activate
```

## Instalar Dependencias
Para instalar las dependencias de la aplicación, ejecuta el siguiente comando en la terminal:
```bash
pip install -r requirements.txt
```

## Acceso a la Aplicación

Para acceder a la aplicación, necesitas ejecutarla en tu entorno local. Puedes hacerlo utilizando el comando `uvicorn` en la terminal, asumiendo que estás en el directorio raíz de la aplicación:

```bash
uvicorn main:app --reload
```

Una vez que la aplicación esté en funcionamiento, puedes acceder a la documentación de la API en tu navegador web en la dirección `http://127.0.0.1:8000/docs`.

## Endpoints de la Aplicación

La aplicación tiene los siguientes endpoints:

### GET /movies

Este endpoint devuelve una lista de todas las películas en la base de datos.

### GET /movies/{category}

Este endpoint devuelve una lista de todas las películas que pertenecen a la categoría especificada.

### POST /movies

Este endpoint crea una nueva película en la base de datos. Necesitas proporcionar los detalles de la película en el cuerpo de la solicitud.

### GET /movies/data

Este endpoint carga los datos de las películas desde un archivo JSON en la base de datos.

### PUT /movies/{id}

Este endpoint actualiza los detalles de una película existente en la base de datos. Necesitas proporcionar el ID de la película que deseas actualizar y los nuevos detalles de la película en el cuerpo de la solicitud.

### DELETE /movies

Este endpoint elimina todas las películas de la base de datos.

### DELETE /movies/{id}

Este endpoint elimina una película específica de la base de datos. Necesitas proporcionar el ID de la película que deseas eliminar.

## Modelos de la Aplicación

La aplicación utiliza dos modelos de Pydantic: `Movie` y `User`. El modelo `Movie` se utiliza para validar y serializar los datos de las películas, mientras que el modelo `User` se utiliza para validar y serializar los datos de los usuarios.

## Bases de Datos

La aplicación utiliza SQLAlchemy para interactuar con la base de datos. La base de datos contiene una tabla `movies` que almacena los detalles de las películas.

## Middleware

La aplicación utiliza un middleware JWT Bearer para manejar la autenticación de los usuarios.

## Referencias

Para obtener más información sobre cómo utilizar FastAPI, puedes consultar la [documentación oficial de FastAPI](https://fastapi.tiangolo.com/).

Para obtener más información sobre cómo utilizar SQLAlchemy, puedes consultar la [documentación oficial de SQLAlchemy](https://docs.sqlalchemy.org/en/14/).

Para obtener más información sobre cómo utilizar JWT Bearer, puedes consultar la [documentación oficial de JWT Bearer](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/).

Para obtener más información sobre cómo utilizar Pydantic, puedes consultar la [documentación oficial de Pydantic](https://pydantic-docs.helpmanual.io/).

Para obtener más información sobre cómo utilizar Uvicorn, puedes consultar la [documentación oficial de Uvicorn](https://www.uvicorn.org/).

[Source 0](https://fastapi.tiangolo.com/reference/apirouter/)
[Source 2](https://apidog.com/articles/how-to-use-fastapi-apirouter/)