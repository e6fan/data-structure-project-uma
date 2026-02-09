class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)] 
    def HashFunction(self, key):
        return hash(key) % self.size
    def Insert(self, key, value):
        index = self.HashFunction(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    def Search(self, key):
        index = self.HashFunction(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None  
    def Remove(self, key):
        index = self.HashFunction(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return v
        return None 
