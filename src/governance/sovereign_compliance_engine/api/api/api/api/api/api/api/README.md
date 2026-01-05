# Regulator Read-Only REST API

## Purpose
Provide **non-mutable, auditable, regulator-grade** access to:
- Governance audit logs
- Authority registry
- Jurisdictional enforcement history

## Security Model
- API Key (read-only)
- No POST / PUT / DELETE
- No mutation endpoints
- Explicit regulator authentication

## Endpoints
GET /regulator/audit/logs  
GET /regulator/audit/logs/{hash}  
GET /regulator/authorities  

## Guarantees
- No state modification
- No hidden enforcement
- Full forensic traceability
