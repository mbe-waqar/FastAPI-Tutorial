from pydantic import BaseModel

class Patient(BaseModel):
    name : str
    age : int

def insert_patient(patient: Patient):
    
    print(f"Patient Name: {patient.name}, Age: {patient.age}")
    print("Patient inserted successfully!")

def update_patient(patient: Patient):
    print(f"Name: {patient.name}, Age: {patient.age}")
    print("Patient updated successfully!")

patient_info = {
    "name": "John Doe",
    "age": 30
}

patient1 = Patient(**patient_info)

insert_patient(patient1)
update_patient(patient1)