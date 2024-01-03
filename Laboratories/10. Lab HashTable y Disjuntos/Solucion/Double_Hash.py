class HashTableSecond:
    def __init__(self):
        self.elements = []

    def printElements(self):
        for element in self.elements:
            print(element)
        print()

    def insert(self, element):
        self.elements.append(element)

    def search(self, key):
        for e in self.elements:
            if e[0] == key:
                return e[1]
        return None

    def update(self, key, value2):
        for e in self.elements:
            if e[0] == key:
                e[1] = value2

    def delete(self, key):
        element = self.search(key)
        if element:
            self.elements.remove(element)


class HashTableWithSecondaryHash:
    def __init__(self, size):
        self.elements = [HashTableSecond() for _ in range(size)]

    def getElements(self):
        return self.elements

    def printElements(self):
        for index, hash_table in enumerate(self.elements):
            print(index, ': ', end='')
            hash_table.printElements()

    def hash(self, key):
        return hash(key) % len(self.elements)

    def assign(self, index, element):
        self.elements[index].insert(element)

    def insert(self, key, value):
        index = self.hash(key)
        print('Inserting', value, 'with key', key, 'on index', index)
        self.assign(index, (key, value))

    def search(self, key):
        index = self.hash(key)
        return self.elements[index].search(key)

    def update(self, key, value2):
        index = self.hash(key)
        self.elements[index].update(key, value2)

    def delete(self, key):
        index = self.hash(key)
        self.elements[index].delete(key)


def main():
    randomPairs = [ (('Colombia', '1243', 'Max'), 'alexei@mail.com'),
                    (('París', '456', 'Ernesto'), 'scmr@yahoo.es'),
                    (('Mexico', '764', 'Patricia'), 'elemental@outlook.com'),
                    ]

    hashtable = HashTableWithSecondaryHash(13)
    for e in randomPairs:
        hashtable.insert(e[0], e[1])

    hashtable.printElements()

    print('Searching for ', ('Colombia', '1243', 'Max'), ': ', hashtable.search(('Colombia', '1243', 'Max')))


main()