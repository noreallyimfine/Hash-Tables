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
            # chain through LL at that index
            current = self.storage[index]
            while current.next:
                # if find key, change element to new value
                if self.storage[index].key == element.key:
                    self.storage[index] = element
                    break
                else:
                    current = current.next
            # if not, add as last element

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
        # if key not found, return None
        if not self.storage[hashed_key]:
            return None
        # if theres no next element, return the hashed_keys value
        elif self.storage[hashed_key].next is None:
            return self.storage[hashed_key].value
        # if there is a next:
        else:
            # compare keys until we find the right one
            current = self.storage[hashed_key]
            while current.key != key:
                # print(current)
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
        old_storage = self.storage
        self.storage = [None] * self.capacity
        # for item in storage
        for k in old_storage:
            # only one list pointer item is stored
            # check if there is a next element
            # if there is no next element
            if k and not k.next:
                # insert into storage (key, value)
                self.insert(k.key, k.value)
            # if there is
            elif k and k.next:
                while k:
                    self.insert(k.key, k.value)
                    k = k.next


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
