from pydantic import BaseModel

class RawRecord(BaseModel):
    name: str
    value: float
