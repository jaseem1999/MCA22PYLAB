#Store a list of first names. Count the occurrences of ‘a’ within the list.

list_name = ["apple","banana","apple","cherry","apple","banana"]
list_name_count = [i.count(x) for x in list_name for i in x if i in "a"]
print("All list ",list_name)
print("Count list ",list_name_count)

