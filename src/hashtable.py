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
        # hash the value
        index = self._hash_mod(key)
        # make a Linked Pair obj of (key, value)
        element = LinkedPair(key, value)

        # if there already is an element in that index
        if self.storage[index] is not None:
            # value at index will point to new element
            self.storage[index].next = element
        else:
            self.storage[index] = element

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # if key not found, print warning
        hashed_key = self._hash_mod(key)
        if self.storage[hashed_key] is None:
            print("ERROR: key not in table")
            return
        # if key is found
        else:
            # if there is a connected node, element becomes next
            if self.storage[hashed_key].next:
                self.storage[hashed_key] = self.storage[hashed_key].next
            # else just change it back to None
            else:
                self.storage[hashed_key] = None

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # hash key to find index
        hashed_key = self._hash_mod(key)
        if self.storage[hashed_key] is None:
            return None
        # if theres no next element, return the hashed_keys value
        if self.storage[hashed_key].next is None:
            return self.storage[hashed_key].value
        # if there is a next:
        else:
            # compare keys until we find the right one
            current = self.storage[hashed_key]
            while current.key != key:
                current = current.next
            # return value of matching key
            return current.value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # new storage list double length of original capacity
        self.capacity *= 2
        new_storage = [None] * self.capacity
        # for item in storage
        for k in self.storage:
            # if one item in index
            if not k.next:
                # move item to new storage
                new_hash = self._hash_mod(k.key)
                new_lp = LinkedPair(k.key, k.value)
                new_storage[new_hash] = new_lp
            # if more than one
            else:
                while k.next:
                    # temp store next element
                    nxt = k.next
                    # move current element to new storage
                    new_hash = self._hash_mod(k.key)
                    new_lp = LinkedPair(k.key, k.value)
                    new_storage[new_hash] = new_lp
                    # repeat until no next
                    k = nxt
        self.storage = new_storage


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
