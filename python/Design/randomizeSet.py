class RandomizedSet:

    def __init__(self):
        self.indices = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.vals.append(val)
        self.indices[val] = len(self.vals)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        # Get index of the val that need to removed
        i = self.indices[val]
        
        # Update the index of vals[-1] in the indices.
        self.indices[self.vals[-1]] = i
        
        # Move the last element to the i th position.
        self.vals[i] = self.vals[-1]
        
        # Remove the index of val from indices
        # Remove the last element from vals
        del self.indices[val]
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.vals)