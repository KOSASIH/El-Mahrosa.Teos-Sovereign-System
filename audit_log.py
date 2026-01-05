from typing import List
from .audit_event import AuditEvent


class AuditLog:
    def __init__(self):
        self._events: List[AuditEvent] = []

    def append(self, event: AuditEvent):
        self._events.append(event)

    def all_event_hashes(self) -> List[bytes]:
        return [event.hash() for event in self._events]

    def __len__(self):
        return len(self._events)
