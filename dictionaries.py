#dictionaries have index which is not an integer

#represented by curly brace

#keys are unique can be immutable objects such as tuple

#values can be immutable, mutable and duolicates

#each key and value pair is seprated by a comma 

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}

#can access value by key 
print(Dict['key4'])