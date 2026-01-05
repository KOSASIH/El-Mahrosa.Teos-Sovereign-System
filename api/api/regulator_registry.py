from dataclasses import dataclass
from typing import Dict
from .hardware_identity import HardwareIdentity


@dataclass(frozen=True)
class RegulatorIdentity:
    regulator_id: str
    hardware_identity: HardwareIdentity
    certificate_fingerprint: str
    active: bool = True


# === IMMUTABLE REGISTRY (replace with DB / ledger) ===
REGULATOR_REGISTRY: Dict[str, RegulatorIdentity] = {}


def register_regulator(identity: RegulatorIdentity):
    REGULATOR_REGISTRY[identity.certificate_fingerprint] = identity


def resolve_regulator(cert_fingerprint: str) -> RegulatorIdentity | None:
    return REGULATOR_REGISTRY.get(cert_fingerprint)
