from pydantic import BaseModel
from typing import Literal

class MetaData(BaseModel):
    model: str
    tokens: int
class ChatMessage (BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str
    timestamp: int
    metadata: MetaData | None = None

msg = ChatMessage(
    role="system",
    content="Hello",
    timestamp=1700000000,
    metadata={"model": "claude-sonnet-4-6", "tokens": 5}
)

print(msg.model_dump_json(indent=2))
