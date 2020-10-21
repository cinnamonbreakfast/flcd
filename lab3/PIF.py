from hashtable import HashTable

class PIF:
    def __init__(self):
        self._data = []

    def add(self, key, pos):
        return self._data.append((key, pos))

    def __str__(self):
        q = ''
        for i in self._data:
            q += str(i) + "\n"

        return q

