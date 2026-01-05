from fastapi import APIRouter, Depends, Query, HTTPException
from typing import List

from .security import regulator_auth
from .models import AuditRecordResponse, AuthorityResponse
from .storage import (
    get_audit_logs,
    get_audit_by_hash,
    get_authorities
)

router = APIRouter(prefix="/regulator", tags=["Regulator API"])


@router.get(
    "/audit/logs",
    response_model=List[AuditRecordResponse],
    dependencies=[Depends(regulator_auth)]
)
def read_audit_logs(limit: int = Query(50, le=500)):
    """
    Retrieve immutable audit records.
    """
    return get_audit_logs(limit)


@router.get(
    "/audit/logs/{record_hash}",
    response_model=AuditRecordResponse,
    dependencies=[Depends(regulator_auth)]
)
def read_audit_record(record_hash: str):
    """
    Retrieve a specific audit record by hash.
    """
    record = get_audit_by_hash(record_hash)
    if not record:
        raise HTTPException(status_code=404, detail="Audit record not found")
    return record


@router.get(
    "/authorities",
    response_model=List[AuthorityResponse],
    dependencies=[Depends(regulator_auth)]
)
def read_authorities():
    """
    List registered authorities.
    """
    return get_authorities()
