print("Getting the data type using type() method: ")
x = 5
print(x)
print(type(x))

print("setting specific data types and getting types: ")

x = str("Hello World")
print(x)
print(type(x))

x = int(20)
print(x)
print(type(x))

x = float(20.5)
print(x)
print(type(x))

x = complex(1j)
print(x)
print(type(x))

x = list(["apple", "banana", "cherry"])
print(x)
print(type(x))

x = tuple(("apple", "banana", "cherry"))
print(x)
print(type(x))

x = range(6)
print(x)
print(type(x))

x = dict({"name" : "John", "age" : 36})
print(x)
print(type(x))

x = set({"apple", "banana", "cherry"})
print(x)
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

x = bool(True)
print(x)
print(type(x))

x = bytes(b"Hello")
print(x)
print(type(x))

x = bytearray(5)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x))


