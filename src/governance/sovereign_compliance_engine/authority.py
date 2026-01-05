from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

class AuthorityRole(Enum):
    FOUNDER = "founder"
    REGULATOR = "regulator"
    OPERATOR = "operator"
    AUDITOR = "auditor"
    CITIZEN = "citizen"
    SYSTEM = "system"

@dataclass(frozen=True)
class Authority:
    authority_id: str
    role: AuthorityRole
    public_key: str
    jurisdiction: str
    activated_at: datetime
    expires_at: Optional[datetime] = None

    def is_active(self, now: datetime) -> bool:
        if self.expires_at and now > self.expires_at:
            return False
        return now >= self.activated_at
