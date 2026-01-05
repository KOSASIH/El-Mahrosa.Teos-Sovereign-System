from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AuditRecordResponse(BaseModel):
    event_id: str
    authority_id: str
    action: str
    jurisdiction: str
    timestamp: datetime
    previous_hash: Optional[str]
    hash: str


class AuthorityResponse(BaseModel):
    authority_id: str
    role: str
    jurisdiction: str
    active_from: datetime
    active_until: Optional[datetime]
