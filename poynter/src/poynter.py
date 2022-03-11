from datetime import datetime
import random


size_t = int


class SegmentationFault(Exception):
    """ No pointer could be complete without a segmentation fault """
    pass


class Pointer:
    def __init__(self, size: size_t):
        self.size = size
        # because out of bounds access should be possible just like in C
        self.data = [None for i in range(size * size * size)]
        self._freed = False

    def __del__(self):
        if not self._freed:
            print(f"Segmentation fault - Core dumped")

    def free(self):
        self._freed = True

    def __getitem__(self, subscript):
        """You will get a Segmentation fault half the time you try to access out of bounds"""
        if subscript >= self.size:
            random.seed(datetime.now())
            is_segfault = random.choice([True, False])
            if is_segfault:
                raise SegmentationFault("Core dumped")
        return self.data[subscript]

    def __setitem__(self, subscript, item):
        self.data[subscript] = item

    def __eq__(self, other):
        for i in range(other.size * other.size * other.size):
            self.size = other.size
            self.data[i] = other.data[i]
        return self


def malloc(size: size_t):
    return Pointer(size)


def free(pointer: Pointer):
    pointer.free()
