from dataclasses import dataclass
from hashlib import sha256


@dataclass(frozen=True)
class HardwareIdentity:
    device_id: str
    manufacturer: str
    attestation_hash: str

    @staticmethod
    def derive(
        device_serial: str,
        manufacturer: str,
        attestation_blob: bytes
    ) -> "HardwareIdentity":
        digest = sha256(attestation_blob).hexdigest()
        return HardwareIdentity(
            device_id=f"{manufacturer}:{device_serial}",
            manufacturer=manufacturer,
            attestation_hash=digest
        )
