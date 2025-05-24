from typing import Optional
from pydantic import BaseModel, Field, computed_field


class Booking(BaseModel):
    id: int
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rates_per_night: float = Field(..., ge=1000, le=25000)
    additional_service_amount: Optional[float] = Field(le=100000, default=0)
    late_checkout: bool = False

    @computed_field
    @property
    def total_amount(self) -> float:
        amount: float = 0

        if self.late_checkout is True:
            amount += 125

        if self.additional_service_amount is not None:
            amount += (self.additional_service_amount * 118) / 100

        amount += (self.rates_per_night * self.nights * 112) / 100

        return amount

    @computed_field
    @property
    def tax_amount(self) -> float:
        amount = 0

        if self.additional_service_amount is not None:
            amount += (self.additional_service_amount * 18) / 100

        amount += (self.rates_per_night * self.nights * 12) / 100

        return amount
