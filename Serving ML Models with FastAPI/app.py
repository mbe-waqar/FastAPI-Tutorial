from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd

# import the ML model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

#pydantic model for input data
class UserInput(BaseModel):
    age:
    weight: