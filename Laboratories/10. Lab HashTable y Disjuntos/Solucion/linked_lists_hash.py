

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class HashTable:
    def __init__(self, size):
        self.size= size
        self.elements = [None]*size


    def getElements(self):
        return self.elements

    def hash(self, key):
        return hash(key) % len(self.elements)

    def assign(self, index, element):
        self.elements[index].append(element)

    def insert(self, key, value):
        index = self.hash(key)
        new_node=Node(key,value)
        if self.elements[index] is None:
            self.elements[index]=new_node
        else:
            cu_nod=self.elements[index]
            while cu_nod.next:
                cu_nod=cu_nod.next
            cu_nod.next=new_node
    def search(self, key):
        index = self.hash(key)
        cu_nod = self.elements[index]

        while cu_nod:
            if cu_nod.key == key:
                return cu_nod.value
            cu_nod= cu_nod.next

        return None

    def update(self, key, value):
        index = self.hash(key)
        cu_nod = self.elements[index]

        while cu_nod:
            if cu_nod.key == key:
                cu_nod.value = value
                return
            cu_nod = cu_nod.next

    def delete(self, key):
        index = self.hash(key)
        cu_nod = self.elements[index]
        prev = None

        while cu_nod:
            if cu_nod.key == key:
                if prev:
                    prev.next = cu_nod.next
                else:
                    self.elements[index] = cu_nod.next
                return
            prev = cu_nod
            cu_nod = cu_nod.next

def main():

    randomPairs = [ (('Colombia', '1243', 'Max'), 'alexei@mail.com'),
                    (('París', '456', 'Ernesto'), 'scmr@yahoo.es'),
                    (('Mexico', '764', 'Patricia'), 'elemental@outlook.com'),
                    ]

    hashtable = HashTable(13)
    for e in randomPairs:
        hashtable.insert(e[0], e[1])
    print('Searching for ', ('Colombia', '1243', 'Max'), ': ', hashtable.search(('Colombia', '1243', 'Max')))


main()

# sha, MD5