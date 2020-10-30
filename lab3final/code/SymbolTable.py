from hashtable import HashTable

class SymbolTable:
    def __init__(self):
        self._ht = HashTable()

    def get(self, key):
        return self._ht.get(key)

    def add(self, key, value):
        return self._ht.add(key, value)
    
    def hash(self, v):
        return self._ht.hash(v)

    def __str__(self):
        return str(self._ht)

    def __iter__(self):
        return iter(self._ht)
