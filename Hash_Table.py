class HashTable:

    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value
    
    def __delitem__(self, index):
        h = self.get_hash(index)
        self.arr[h] = None

ht = HashTable()
ht['sep 20'] = 40
ht['april 25'] = 84
ht['april 28'] = 21 # setting the value
# print(ht.arr)
print(ht['april 28']) # getting the value 
del ht['april 25']
print(ht.arr) #


