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

temp1 = patient1.model_dump()
print(temp1)
print(type(temp1))

temp2 = patient1.model_dump_json()
print(temp2)
print(type(temp2))