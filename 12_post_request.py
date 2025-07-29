from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="The unique ID of the patient", example="P001")]
    name: Annotated[str, Field(..., max_length=100, description="Full name of the patient", example="John Doe")]
    city: Annotated[str, Field(..., description="City of residence", example="New York")]
    age: Annotated[int, Field(..., ge=0, le=120, description="Age of the patient", example=30)]
    gender: Annotated[Literal['male', 'female', 'other'], Field(..., description="Gender of the patient", example="male")]
    height: Annotated[float, Field(..., ge=0, description="Height in meters", example=1.75)]
    weight: Annotated[float, Field(..., gt=0, description="Weight in kilograms", example=70)]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)
    
    @computed_field
    @property
    def version(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"
        




#data loading function
def load_data():
    with open('patients.json', 'r') as file:
        data = json.load(file)
    return data  

def save_data(data):
    with open('patients.json', 'w') as file:
        json.dump(data, file)  

#API endpoints / http methods
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

# path parameters example
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description="The ID of the patient to view", example="P001")):
    #load patient data
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

# query parameters example
@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="Field to sort by height, weight, or bmi"), order : str = Query("asc", description="Order of sorting: asc or desc")):
    
    valid_fields = ["height", "weight", "bmi"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Valid fields are: {', '.join(valid_fields)}")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Order must be 'asc' or 'desc'")
    
    data = load_data()
    sort_order = True if order == "desc" else False
    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=sort_order)
    return sorted_data

@app.post("/add_patient")
def add_patient(patient: Patient):

    # 1- Load existing data
    data = load_data()

    # 2- Check if patient ID already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient ID already exists")
    
    # 3- Add new patient to data
    data[patient.id] = patient.model_dump(exclude=['id'])

    # 4- Save updated data back to file
    save_data(data)

    return JSONResponse(status_code=201, content={"message": "Patient added successfully", "patient_id": patient.id})
