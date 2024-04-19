from random import choice

class RandomizedSet:

    def __init__(self):
        self.set = set()

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set.add(val)
        return True


    def remove(self, val: int) -> bool:
        try:
            self.set.remove(val)
            return True
        except KeyError:
            return False

    def getRandom(self) -> int:
        return choice(list(self.set))


randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))
print(randomizedSet.remove(2))
print(randomizedSet.insert(2))
print(randomizedSet.getRandom())
print(randomizedSet.remove(1))
print(randomizedSet.insert(2))
print(randomizedSet.getRandom())

