from fastapi import FastAPI
from routers import route_todo, route_auth
from schemas import SuccessMSG


app = FastAPI()
app.include_router(route_todo.router)
app.include_router(route_auth.router)


@app.get('/', response_model=SuccessMSG)
def root():
  return {"message": "Hello World"}