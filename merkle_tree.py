import hashlib
from typing import List


def sha256(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()


class MerkleTree:
    def __init__(self, leaves: List[bytes]):
        if not leaves:
            raise ValueError("Merkle tree requires at least one leaf")
        self.leaves = [sha256(leaf) for leaf in leaves]
        self.levels = self._build_tree(self.leaves)

    def _build_tree(self, leaves: List[bytes]) -> List[List[bytes]]:
        levels = [leaves]
        while len(levels[-1]) > 1:
            current = levels[-1]
            next_level = []

            for i in range(0, len(current), 2):
                left = current[i]
                right = current[i + 1] if i + 1 < len(current) else left
                next_level.append(sha256(left + right))

            levels.append(next_level)
        return levels

    @property
    def root(self) -> str:
        return self.levels[-1][0].hex()
