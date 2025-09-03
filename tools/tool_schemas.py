from typing import Dict, List, Literal
from pydantic import BaseModel


class Property(BaseModel):
    type: Literal["string"]
    description: str


class Parameters(BaseModel):
    type: Literal["object"]
    properties: Dict[str, Property]
    required: List[str]
    additionalProperties: bool


class FunctionSchema(BaseModel):
    type: Literal["function"]
    name: str
    description: str
    parameters: Parameters
    strict: bool
