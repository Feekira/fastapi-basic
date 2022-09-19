from typing import Optional
from pydantic import BaseModel

class Car(BaseModel):
    name: str
    price: float

class UpdateCar(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None