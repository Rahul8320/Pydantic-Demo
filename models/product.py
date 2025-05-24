from typing import Optional
from pydantic import BaseModel, computed_field


class Product(BaseModel):
    name: str
    price: float
    quantity: int
    desc: Optional[str] = None

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
