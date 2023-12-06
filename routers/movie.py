from fastapi import APIRouter, Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import Optional, List
from config.database import Session, Base
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from schemas.movie import Movie
from schemas.user import User
import json

movie_router = APIRouter()
with open('.\MOCK_DATA.json', 'r') as file:
    movies_data = json.load(file)

#endopoint de la API
url = 'http://127.0.0.1:8000/movies/'

@movie_router.get("/movies", tags=['Movies'], response_model=List[Movie], status_code=200)#,dependencies=[Depends(JWTBearer())]) 
def get_movies() -> List[Movie]:
    db = Session()
    result = db.query(MovieModel).all()
    response = JSONResponse(content=jsonable_encoder(result), status_code=200)

    return response

@movie_router.get("/movies/", tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=12)):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.category == category).all()
    response = JSONResponse(content=jsonable_encoder(result), status_code=200)
    if not result:
        response = JSONResponse(content={"message": "Category not found"}, status_code=404)
    return response

@movie_router.get("/movie")
def get_gnrMovie(gnr: str):
    db = Session()
    #fiter_by gender
    result = db.query(MovieModel).filter(MovieModel.category == gnr).all()
    response = JSONResponse(content=jsonable_encoder(result), status_code=200)
    if not result:
        response = JSONResponse(content={"message": "Category not found"}, status_code=404)
    return response

 

@movie_router.post("/movies", tags=['Movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie):
    db = Session()
    new_movie = MovieModel(**movie.model_dump())
    db.add(new_movie)
    db. commit ()
    return JSONResponse(content={"message": "Movie created successfully"},
                        status_code=201)

@movie_router.get("/movies/data", tags=['Movies'], response_model=List[Movie], status_code=200)
def post_Movie_Data_Base()-> List[Movie]:
  db = Session()
  allMovie = movies_data
  errors=[]
  for movie in allMovie:
      #print(movie)
      try:
          movie_model = Movie(**movie)
          new_movie = MovieModel(**movie_model.dict())
          db.add(new_movie)
          db.commit()
      except Exception as e:
          errors.append(movie)
   
  result = db.query(MovieModel).all()
  print("Movies Not added:",errors)
  response = JSONResponse(content=jsonable_encoder(result), status_code=200)
  return response



@movie_router.put("/movies/{id}",tags=['Movies'])
def update_movie(id: int, movie: Movie):
    db = Session()
    movie_update = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not movie_update:
        return JSONResponse(content={"message": "Movie not found"}, status_code=404)
    
    movie_update.title = movie.title
    movie_update.overview = movie.overview
    movie_update.year = movie.year
    movie_update.rating = movie.rating
    movie_update.category = movie.category
    db.commit()
    return JSONResponse(content={"message": "Movie updated successfully"}, status_code=200)


@movie_router.delete("/movies/", tags=['Movies'], response_model=dict)
def delete_all_movies():
    db = Session()
    db.query(MovieModel).delete()
    db.commit()
    return JSONResponse(content={"message": "All movies deleted successfully"}, status_code=200)



@movie_router.delete("/movie/{id}",tags=['Movies'], response_model= dict)
def deleteMovie(id: int):
    db = Session()
    movie = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not movie:
        return JSONResponse(content={"message": "Movie not found"}, status_code=404)
    db.delete(movie)
    db.commit()
    return JSONResponse(content = {"message": "Movie deleted successfully"}, status_code = 200)

