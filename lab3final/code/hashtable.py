

class HashTable:
    def __init__(self, len = 4):
        self._array = []
        for i in range(len):
            self._array.append([])

    def hash(self, key):
        '''
        Use python hash function and len to get the index
        :param key: object
        :return: number
        '''
        ln = len(self._array)
        return hash(key) % ln

    def add(self, key, value):
        '''
        Add a key, value pair to the hash table
        :param key: object
        :param value: object
        :return: index
        '''
        index = self.hash(key)

        if [key, value] in self._array[index]:
            raise ValueError()

        self._array[index].append([key, value])
        
        return self.get_pos(key)

    def get(self, key):
        '''
        Get the value of a key
        :param key: object
        :return: object
        :throw: KeyError
        '''
        index = self.hash(key)

        if len(self._array[index]) == 0:
            raise KeyError("1")
        else:
            for pair in self._array[index]:
                if pair[0] == key:
                    return pair[1]

            raise KeyError("2")

    def get_pos(self, key):
        index = self.hash(key)

        if len(self._array[index]) == 0:
            raise KeyError("1")
        else:
            pos = 0
            while pos < len(self._array[index]):
                if self._array[index][pos][0] == key:
                    return pos
                pos += 1

            raise KeyError("2")

    def remove(self, key, value):
        index = self.hash(key)

        if len(self._array[index]) == 0:
            return None
        else:
            for pair in self._array[index]:
                if pair[0] == key:

                    self._array[index] = list(filter(lambda each: each[1] != value, self._array[index]))

                    return pair[1]

            return None

    def __str__(self):
        q = ''
        for i in self._array:
            q += str(i) + "\n"

        return q

    def __iter__(self):
        return iter(self._array)

def test():
    ht = HashTable()
    a = "abc"
    b = "bac"

    print(ht.add(a, 12))
    print(ht.add(b, 32))
    print(ht.add("5", 44))

    # print(ht.get("abc"), " expects 12")
    # print(ht.get(a), " expects 12")
    #
    # print(ht.get("bac"), " expects 32")
    # print(ht.get(b), " expects 32")
    #
    # print(ht.get("5"), " expects 44")
    # print(ht.get_pos("5"), " expects 44")

    print(ht)

# test()