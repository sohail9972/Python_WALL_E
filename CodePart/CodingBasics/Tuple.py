my_tuple = ("a","b","c")
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)

repeated_tuple = tuple1 * 3
print(repeated_tuple)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1])

nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)
print(nested_tuple[1][1])


for i in my_tuple:
    print(i)