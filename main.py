from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from middlewares.error_handler import ErrorHandlerMiddleware
from config.database import engine, Base
from routers.movie import movie_router
from routers import auth



#se crea la instancia de FastApi, (aplicacion)
app = FastAPI()
# Cambio en la documentación
app.title = "My app"
app.version = "1.0.2"
app.add_middleware(ErrorHandlerMiddleware)
app.include_router(movie_router)
app.include_router(auth.auth)


Base.metadata.create_all(bind=engine)


@app.get("/",tags=['Home'])
def message():
    return HTMLResponse(content="<h1>HOME</h1>")

