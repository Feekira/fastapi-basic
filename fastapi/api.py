from re import search
from fastapi import FastAPI
from data import data
from basemodels import *

app = FastAPI()

@app.get("/")
def hello_word():
    return {"Hello":"World"}

@app.get("/get-car-by/{id}")
def get_car(id:int):
    
    search = list(filter(lambda x:x["id"] == id, data))
    
    if search == []:
        return {'Error': 'This model car does not exist'}

    return {"Car ":search[0]}


@app.get("/get-car-by-name")
def get_car_name(name: str):

    print(name)
    search = list(filter(lambda x:x["name"] == name,data))

    if search == []:
        return {'Error':'This name by car dont exist'}

    return {"Car" :search[0]}

@app.get("/list-cars")
def list_cars():
    return {"Cars" :data}


@app.post("/create-car{id}")
def create_car(id:int , car: Car):

    search= list(filter(lambda x: x["id"] == id, data))

    if search != []:
        return {'Error': 'Item exists'}

    car = car.dict()
    car["id"] = id
    data.append(car)

    return car

@app.put("/update-car{id}")
def update_car(id:int, car:UpdateCar):

    search= list(filter(lambda x: x["id"] == id, data))


    if search == []:
        return {'Item': 'Does not exist'}

    if car.name is not None and car.price is not None:
        search[0]['name'] = car.name
        search[0]['price'] = car.price

    return search

@app.delete("/delete-car{id}")
def delete_car(id:int):

    search = list((filter(lambda x: x["id"] == id, data)))

    for i in range(len(data)):
        if search[i]["id"] == id:
            del search[i]
            break

    return {'Message': 'Item deleted successfully'}
