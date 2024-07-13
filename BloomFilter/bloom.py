from bitarray import bitarray


class Bloom:
    def __init__(self, size, hash_count):
        self.hash_count = hash_count
        self.bit_arr = bitarray(size)

    def add_element(self, element):
        pass

    def lookup_element(self, element):
        pass
