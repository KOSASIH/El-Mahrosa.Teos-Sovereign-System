import json, hashlib
from datetime import datetime
from typing import Dict

class AuditLog:
    @staticmethod
    def create(event_type: str, data: Dict) -> Dict:
        entry = {
            "event": event_type,
            "data": data,
            "timestamp": datetime.utcnow().isoformat()
        }
        digest = hashlib.sha256(
            json.dumps(entry, sort_keys=True).encode()
        ).hexdigest()
        entry["hash"] = digest
        return entry
