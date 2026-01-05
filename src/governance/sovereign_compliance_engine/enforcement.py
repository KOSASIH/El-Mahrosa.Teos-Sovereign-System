from .audit_log import AuditLog
from .state_registry import StateRegistry

class EnforcementEngine:
    @staticmethod
    def freeze(entity_id: str, reason: str):
        StateRegistry.set_state(entity_id, "frozen")
        return AuditLog.create("FREEZE", {
            "entity": entity_id,
            "reason": reason
        })

    @staticmethod
    def allow(entity_id: str):
        return AuditLog.create("ALLOW", {"entity": entity_id})
