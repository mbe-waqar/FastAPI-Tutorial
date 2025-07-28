from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Dict, List, Optional, Annotated

class Patient(BaseModel):
    name : Annotated[str, Field(max_length=100, title="Patient Name", description="Full name of the patient", example=["John Doe", "Jane Smith"])]
    age : int
    email: EmailStr
    height: float
    weight: float = Field(gt=0)
    allergies: Optional[List[str]] = None
    contact_info: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        
        valid_domains = ["hdfc.com", "icicibank.com"]
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Email domain must be one of {', '.join(valid_domains)}")
        
        return value
    
    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        return value.upper()
    
    @field_validator('age', mode='before')
    @classmethod
    def age_validator(cls, value):
        if 0 < value < 120:
            return value
        raise ValueError("Age must be between 1 and 119")
    
    

def insert_patient(patient: Patient):
    print(f"Patient Name: {patient.name}, Age: {patient.age}, Height: {patient.height}, Weight: {patient.weight}, Allergies: {patient.allergies}, Contact Info: {patient.contact_info}, Email: {patient.email}")
    print("Patient inserted successfully!")

def update_patient(patient: Patient):
    print(f"Name: {patient.name}, Age: {patient.age}, Height: {patient.height}, Weight: {patient.weight}, Allergies: {patient.allergies}, Contact Info: {patient.contact_info}, Email: {patient.email}")
    print("Patient updated successfully!")

patient_info = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@hdfc.com",
    "height": 175.5,
    "weight": 70.0,
    "contact_info": {"phone": "123-456-7890"}
}

patient1 = Patient(**patient_info)

insert_patient(patient1)
update_patient(patient1)