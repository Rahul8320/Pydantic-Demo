from models.employee import Employee


def main():
    print("Hello from pydantic!")

    employee: dict[str, str | int] = {
        "id": 12,
        "name": "Rahul Dey",
        "salary": 45000,
    }

    print(Employee(**employee))  # type: ignore


if __name__ == "__main__":
    main()
