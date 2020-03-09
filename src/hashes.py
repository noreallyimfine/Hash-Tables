import hashlib

n = 10
key = b"my_value"
key2 = "string".encode()
key3 = b"lunchtime"

index = hash(key) % 8
print(index)
index2 = hash(key2) % 8
print(index2)
index3 = hash(key3) % 8
print(index3)
# for i in range(n):
#     print(hash(key))
#     print(hashlib.sha256(key).hexdigest())
