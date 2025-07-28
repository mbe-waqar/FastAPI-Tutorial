from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as file:
        data = json.load(file)
    return data    

@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"message": "A fully functional API for managing patient data."}

@app.get("/view")
def view():
    data = load_data()
    return data

