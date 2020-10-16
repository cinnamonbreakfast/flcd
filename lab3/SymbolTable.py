from hashtable import HashTable

class SymbolTable:
    def __init__(self):
        self._ht = HashTable()

    def get(self, key):
        return self._ht.get(key)

    def add(self, key, value):
        return self._ht.add(key, value)
