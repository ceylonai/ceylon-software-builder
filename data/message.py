from datetime import datetime

from pydantic import BaseModel, Field


class Message(BaseModel):
    message: str = Field(min_length=1, max_length=100)
    sender: str = Field(min_length=1, max_length=100)
    time: datetime = Field(default_factory=datetime.now)
    type: str = Field(min_length=1, max_length=100)
