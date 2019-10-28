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


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


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

            temp.next=LinkedPair(key,value)



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
                curr.next=curr.next.next
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


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        newCap=self.capacity*2
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
