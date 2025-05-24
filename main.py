from typing import Dict
from models.booking import Booking
from models.employee import Employee
from models.product import Product
from models.user import SignupDto, User


def main() -> None:
    print("Hello from pydantic!")

    employee: Dict[str, str | int] = {
        "id": 12,
        "name": "Rahul Dey",
        "salary": 45000,
    }

    print(Employee(**employee))  # type: ignore

    user: Dict[str, str] = {"username": "test"}
    print(User(**user))

    signupDto: Dict[str, str] = {
        "password": "password",
        "confirm_password": "password",
    }
    print(SignupDto(**signupDto))

    product: Dict[str, str | int | float] = {
        "name": "Samsung s25 ultra",
        "price": 125000,
        "quantity": 10,
    }
    print(Product(**product))  # type: ignore

    booking: Dict[str, int | float | bool] = {
        "id": 123,
        "user_id": 324567,
        "room_id": 101,
        "nights": 2,
        "rates_per_night": 3000,
        "additional_service_amount": 2000,
        "late_checkout": True,
    }
    print(Booking(**booking))  # type: ignore


if __name__ == "__main__":
    main()
