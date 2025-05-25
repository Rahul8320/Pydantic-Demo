from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    address: Address
    roles: List[str] = []
    created_at: datetime

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")}
    )


# create a user instance
def main():
    address = Address(street="center park 26/5", city="Vokanda", zip_code="VOK_49L")
    user = User(
        id=1,
        name="Rahul Dey",
        email="rahul@admin.com",
        address=address,
        roles=["admin", "user"],
        created_at=datetime(2022, 4, 26, 17, 49),
    )

    # using model_dump() -> dict
    user_dict = user.model_dump()
    print(user_dict)
    print("\n------------------------------------------------------------\n")

    # using model_dump_json() -> str
    user_json = user.model_dump_json()
    print(user_json)


if __name__ == "__main__":
    main()
