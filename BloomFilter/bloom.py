import mmh3
from bitarray import bitarray
from typing import List


class Bloom:
    def __init__(self, size: int, hash_count: int):
        self.hash_count = hash_count
        self.size = size
        self.bit_arr = bitarray(size)

    def add_elements(self, elements: List[str]) -> None:
        for element in elements:
            for i in range(self.hash_count):
                index = self.hash_function(element, i)
                print(index)
                self.bit_arr[index] = 1

    def lookup_element(self, element: str) -> bool:
        pass

    def hash_function(self, element: str, seed: int) -> int:
        hash_value = mmh3.hash(element, seed)
        return hash_value % self.size
