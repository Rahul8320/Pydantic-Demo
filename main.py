from typing import Dict
from models.employee import Employee
from models.user import SignupDto, User


def main():
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


if __name__ == "__main__":
    main()
