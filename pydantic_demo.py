
from pydantic import BaseModel, Field, Literal
from pydantic import ValidationError

class User(BaseModel):
    name: str
    age: int = Field(ge=0, le=150)
    email: str | None = None

u = User(name="haydon", age=30)
print(u)

print(u.model_dump())
print(u.model_dump_json())

u2 = User(name="alice", age="25")
print(u2.age, type(u2.age))


try:
    bad = User(name="bob", age=-5)
except ValidationError as e:
    print("校验失败:")
    print(e)

class Address(BaseModel):
    city: str
    zip_code: str
class UserWithAddress(BaseModel):
    name: str
    address: Address

u3 = UserWithAddress(
    name="haydon",
    address={"city": "Shanghai", "zip_code": "200000"}
)

print(u3.model_dump_json(indent=2))




