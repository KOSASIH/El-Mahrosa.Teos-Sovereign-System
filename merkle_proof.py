import hashlib
from typing import List


def sha256(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()


class MerkleProof:
    def __init__(self, leaf: bytes, index: int, siblings: List[bytes]):
        self.leaf = leaf
        self.index = index
        self.siblings = siblings

    def verify(self, expected_root: str) -> bool:
        current = sha256(self.leaf)
        idx = self.index

        for sibling in self.siblings:
            if idx % 2 == 0:
                current = sha256(current + sibling)
            else:
                current = sha256(sibling + current)
            idx //= 2

        return current.hex() == expected_root
