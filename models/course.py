from typing import List, Optional
from pydantic import BaseModel, Field, computed_field


class Lesson(BaseModel):
    id: int
    topic: str


class Module(BaseModel):
    id: int
    name: str
    lessons: List[Lesson]


class Review(BaseModel):
    id: int
    user_id: int
    rating: float = Field(..., le=10, ge=1)
    comment: str = Field(..., min_length=5, max_length=500)
    replies: Optional[List["Review"]] = None


Review.model_rebuild()


class Course(BaseModel):
    id: int
    title: str
    modules: List[Module]
    price: float
    reviews: Optional[List[Review]] = None

    @computed_field
    @property
    def rating(self) -> float:
        if not self.reviews:
            return 0.0

        total = sum(review.rating for review in self.reviews)
        return round(total / len(self.reviews), 1)
