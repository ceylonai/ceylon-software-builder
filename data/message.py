import enum
from datetime import datetime

from pydantic import BaseModel, Field


class Message(BaseModel):
    message: str = Field(min_length=1, max_length=100)
    sender: str = Field(min_length=1, max_length=100)
    time: datetime = Field(default_factory=datetime.now)
    type: str = Field(min_length=1, max_length=100)


class SystemMessageType(str, enum.Enum):
    human_interaction = "human_interaction"
    system_message = "system_message"


class SystemMessage(Message):
    type: str = Field(min_length=1, max_length=100, default=SystemMessageType.system_message)
    content: str = Field(min_length=1, max_length=100)
    time = Field(default_factory=datetime.now)
