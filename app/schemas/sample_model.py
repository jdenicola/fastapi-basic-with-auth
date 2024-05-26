from pydantic import BaseModel


class SampleModel(BaseModel):
    name: str
    id: int
