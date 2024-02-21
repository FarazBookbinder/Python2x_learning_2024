found_dictionary = {"a": 1, "b": 10, "c": 5}
for k,v in found_dictionary.items():
    if k == "b":
        print("b is found")
result = "b" in found_dictionary
result1 = "c" in found_dictionary
result2 = "a" in found_dictionary
print(result,"\n", result1, "\n", result2)
