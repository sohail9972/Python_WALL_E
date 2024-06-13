my_dict = {"name": "John", "age": 30, "city": "New York"}
items= len(my_dict)
print(items)
my_dict["age"]=12

my_dict["country"] = "USA"


del my_dict["city"]
for key,value in my_dict.items():
    print(key ," : ",value)