class RandomizedSet:

    def __init__(self):
        self.s=[]
        self.hashmap={}
        

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.s.append(val)
        self.hashmap[val]=len(self.s)-1
        return True
        

    def remove(self, val: int) -> bool:
        if not val in self.hashmap:
            return False
        
        index=self.hashmap[val]
        self.s[index]=self.s[len(self.s)-1]
        self.hashmap[self.s[len(self.s)-1]]=index
        
        self.s.pop()
        
        del self.hashmap[val]
        
        return True
        

    def getRandom(self) -> int:
        index=random.randint(0, len(self.s)-1)
        return self.s[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()