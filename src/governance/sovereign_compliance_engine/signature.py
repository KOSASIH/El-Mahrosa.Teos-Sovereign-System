from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.exceptions import InvalidSignature

def verify_signature(public_key_pem: str, message: bytes, signature: bytes) -> bool:
    public_key = serialization.load_pem_public_key(
        public_key_pem.encode()
    )
    try:
        public_key.verify(signature, message)
        return True
    except InvalidSignature:
        return False
