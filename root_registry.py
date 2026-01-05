from datetime import datetime
from typing import Dict


class MerkleRootRegistry:
    def __init__(self):
        self._registry: Dict[str, Dict] = {}

    def register_root(
        self,
        merkle_root: str,
        jurisdiction: str,
        authority: str,
    ):
        self._registry[merkle_root] = {
            "jurisdiction": jurisdiction,
            "authority": authority,
            "timestamp": datetime.utcnow().isoformat(),
        }

    def get(self, merkle_root: str) -> Dict | None:
        return self._registry.get(merkle_root)
