from pydantic import BaseModel, Field
from typing import List

class PolicyRule(BaseModel):
    name: str
    condition: str
    action: str
    reason: str
    severity: str = Field(default="medium")

class SovereignPolicy(BaseModel):
    jurisdiction: str
    version: str
    issuer: str
    rules: List[PolicyRule]
