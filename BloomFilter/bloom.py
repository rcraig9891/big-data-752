import mmh3
from bitarray import bitarray
from typing import List


class Bloom:
    def __init__(self, size: int, hash_count: int):
        self.hash_count = hash_count
        self.size = size
        self.bit_arr = bitarray(size)

    def add_element(self, elements: List[str]) -> None:
        for element in elements:
            for i in range(self.hash_count):
                pass

    def lookup_element(self, element: str) -> bool:
        pass
