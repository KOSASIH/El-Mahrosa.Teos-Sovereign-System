from fastapi import Request, HTTPException, status
import hashlib


def extract_client_certificate(request: Request) -> str:
    """
    Extract client certificate fingerprint from mTLS connection.
    Depends on reverse proxy / ASGI server.
    """
    cert_pem = request.headers.get("x-client-cert")
    if not cert_pem:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Client certificate required"
        )

    fingerprint = hashlib.sha256(cert_pem.encode()).hexdigest()
    return fingerprint
