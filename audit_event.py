import json
import hashlib
from datetime import datetime
from typing import Dict


class AuditEvent:
    def __init__(
        self,
        event_type: str,
        subject: str,
        authority: str,
        payload: Dict,
        jurisdiction: str,
        timestamp: str | None = None,
    ):
        self.event_type = event_type
        self.subject = subject
        self.authority = authority
        self.payload = payload
        self.jurisdiction = jurisdiction
        self.timestamp = timestamp or datetime.utcnow().isoformat()

    def canonical_json(self) -> bytes:
        return json.dumps(
            {
                "event_type": self.event_type,
                "subject": self.subject,
                "authority": self.authority,
                "payload": self.payload,
                "jurisdiction": self.jurisdiction,
                "timestamp": self.timestamp,
            },
            sort_keys=True,
            separators=(",", ":"),
        ).encode()

    def hash(self) -> bytes:
        return hashlib.sha256(self.canonical_json()).digest()
