from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address

address_dict = {
    "city": "New York",
    "state": "NY",
    "zip_code": "10001"
}
address1 = Address(**address_dict)

patient_dict = {
    "name": "Alice Smith",
    "age": 30,
    "gender": "Female",
    "address": address1
}
patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.state)   
print(patient1.address.zip_code)