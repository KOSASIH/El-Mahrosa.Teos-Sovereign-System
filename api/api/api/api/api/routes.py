from fastapi import APIRouter, Depends
from typing import List

from .regulator_guard import regulator_mtls_guard
from .models import AuditRecordResponse, AuthorityResponse
from .storage import get_audit_logs, get_authorities

router = APIRouter(prefix="/regulator", tags=["Regulator API"])


@router.get(
    "/audit/logs",
    response_model=List[AuditRecordResponse],
    dependencies=[Depends(regulator_mtls_guard)]
)
def audit_logs(limit: int = 50):
    return get_audit_logs(limit)


@router.get(
    "/authorities",
    response_model=List[AuthorityResponse],
    dependencies=[Depends(regulator_mtls_guard)]
)
def authorities():
    return get_authorities()
