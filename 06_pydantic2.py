from pydantic import BaseModel, EmailStr, Field
from typing import Dict, List, Optional, Annotated

class Patient(BaseModel):
    name : Annotated[str, Field(max_length=100, title="Patient Name", description="Full name of the patient", example=["John Doe", "Jane Smith"])]
    age : int
    height: float
    weight: float = Field(gt=0)
    allergies: Optional[List[str]] = None
    contact_info: Dict[str, str]

def insert_patient(patient: Patient):
    
    print(f"Patient Name: {patient.name}, Age: {patient.age}, Height: {patient.height}, Weight: {patient.weight}, Allergies: {patient.allergies}, Contact Info: {patient.contact_info}")
    print("Patient inserted successfully!")

def update_patient(patient: Patient):
    print(f"Name: {patient.name}, Age: {patient.age}, Height: {patient.height}, Weight: {patient.weight}, Allergies: {patient.allergies}, Contact Info: {patient.contact_info}")
    print("Patient updated successfully!")

patient_info = {
    "name": "John Doe",
    "age": 30,
    "height": 175.5,
    "weight": 70.0,
    "contact_info": {"email": "abc@gmail.com", "phone": "123-456-7890"}
}

patient1 = Patient(**patient_info)

insert_patient(patient1)
update_patient(patient1)