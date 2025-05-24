from typing import Dict, List
from models.booking import Booking
from models.course import Course, Lesson, Module, Review
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


def run() -> None:
    lessons: List[Lesson] = [
        Lesson(id=1, topic="Why we need Pydantic?"),
        Lesson(id=2, topic="Development Configuration"),
    ]

    modules: List[Module] = [Module(id=101, name="Introduction", lessons=lessons)]

    reviews: List[Review] = [
        Review(id=1, user_id=1, rating=8.5, comment="Great course!"),
        Review(id=2, user_id=2, rating=9.0, comment="Really enjoyed it."),
        Review(id=3, user_id=3, rating=5.5, comment="Good but could be better."),
    ]

    course = Course(
        id=105763,
        title="Pydantic Carse Course",
        modules=modules,
        price=199.00,
        reviews=reviews,
    )
    print(course)


if __name__ == "__main__":
    # main()
    run()
