from bitarray import bitarray
from typing import List


class Bloom:
    def __init__(self, size: int, hash_count: int):
        self.hash_count = hash_count
        self.bit_arr = bitarray(size)

    def add_element(self, element: List[str]) -> None:
        pass

    def lookup_element(self, element: str) -> bool:
        pass
