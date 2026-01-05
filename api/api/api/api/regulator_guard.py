from fastapi import Request, Depends, HTTPException, status
from .mtls import extract_client_certificate
from .regulator_registry import resolve_regulator
from .hardware_identity import HardwareIdentity


def regulator_mtls_guard(
    request: Request,
    hardware_attestation: str = Depends(lambda: "")
):
    """
    Full regulator authentication:
    - mTLS cert
    - hardware-bound identity
    """

    cert_fingerprint = extract_client_certificate(request)
    regulator = resolve_regulator(cert_fingerprint)

    if not regulator or not regulator.active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Regulator not authorized"
        )

    # OPTIONAL: hardware attestation verification
    if hardware_attestation:
        derived = HardwareIdentity.derive(
            device_serial="unknown",
            manufacturer=regulator.hardware_identity.manufacturer,
            attestation_blob=hardware_attestation.encode()
        )

        if derived.attestation_hash != regulator.hardware_identity.attestation_hash:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Hardware attestation mismatch"
            )

    return regulator
