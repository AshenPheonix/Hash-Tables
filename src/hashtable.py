# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.load=0
        self.init_capacity=capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return self._hash_djb2(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        ret = 0
        char = 0
        for c in key:
            char = ord(c)
            ret = ((ret<<5) + ret)+char
        return ret


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        keyed = self._hash(key)
        spot = keyed % self.capacity
        if not self.storage[spot]:
            self.load+=1
            self.storage[spot]=LinkedPair(key,value)
        else:
            temp=self.storage[spot]
            if temp.key==key:
                temp.value=value
                return

            while temp.next:
                if temp.next.key==key:
                    temp.next.value=value
                    return
                else:
                    temp=temp.next

            self.load+=1
            temp.next=LinkedPair(key,value)

        if (self.load / self.capacity) >= .7:
            self.resize()


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        spot = self._hash(key) % self.capacity
        curr = self.storage[spot]
        if self.storage[spot].key==key:
            self.storage[spot]=self.storage[spot].next
            return

        while curr.next:
            if curr.next.key==key:
                self.load-=1
                curr.next=curr.next.next
                if self.load/self.capacity<=.2:
                    self.resize('down')
                return
            else:
                curr=curr.next

        print( f"Warning: Key {key} not found")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        spot= self._hash(key) % self.capacity
        fetch=self.storage[spot]
        while fetch:
            if fetch.key==key:
                return fetch.value
            else:
                fetch=fetch.next
        return None


    def resize(self,dir='up'):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        if dir=='up':
            newCap=self.capacity*2
        elif dir=='down':
            newCap=self.capacity//2
            if newCap<self.init_capacity:
                return

        newStore=[None]*newCap
        reserve=self.storage
        self.storage=newStore
        self.capacity=newCap
        for item in reserve:
            temp=item
            while temp:
                self.insert(temp.key,temp.value)
                temp=temp.next
            



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
