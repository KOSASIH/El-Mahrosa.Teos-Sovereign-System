"""
Read-only storage abstraction.
Can be backed by DB, IPFS, Ledger, or archive.
"""

from typing import List
from ..audit_log import AuditRecord
from ..authority import Authority

# === TEMPORARY IN-MEMORY STORE (replace in prod) ===
AUDIT_LOG_STORE: List[AuditRecord] = []
AUTHORITY_STORE: List[Authority] = []


def get_audit_logs(limit: int = 100) -> List[AuditRecord]:
    return AUDIT_LOG_STORE[-limit:]


def get_audit_by_hash(record_hash: str) -> AuditRecord | None:
    for r in AUDIT_LOG_STORE:
        if r.hash == record_hash:
            return r
    return None


def get_authorities() -> List[Authority]:
    return AUTHORITY_STORE
