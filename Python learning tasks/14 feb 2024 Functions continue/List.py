#What is List?
# List is collection of item (Duplicate is allowed in list)
my_list = [1,2,3]
my_list2 = [1, "Faraz", 20.3, True]
#change the element of of my_list.
my_list[1] = 20

print("Element at index 0 is:-", my_list[0],"\n", my_list2[1])
print("Element at index 0 is:-", my_list,"\n", my_list2)

#now append(Join the another value with existing list)
my_list.append(90)
my_list2.append('False')
print("This is the new value which is added later:-", my_list)
print("This is the new value which is added later:-", my_list2)

#Extend the list
my_list.extend([55,67,30])
my_list2.extend([55.3,67.02,"Sukun"])
print("This is the new list which is added later:-", my_list)
print("This is the new list which is added later:-", my_list2 )

#insert in the list
my_list.insert(1,"a")
print("New inserted value is:-", my_list)

#Remove the value from the list
my_list.remove("a")
print("List after removing 'a':-", my_list)

#Copy the list
my_copy_list = my_list.copy()
print("This is the copy of the list:-", my_list)

#Clear list
my_list = my_list.clear()
print("List is cleared now:-", my_list)
print("This is the copy of the list:-", my_copy_list)
print("Print index of 3 in the list:-", my_list)

#sort the list
my_copy_list.sort()
print("List after sorting is:-", my_copy_list)

# List reverse
my_copy_list.reverse()
print("List after reverse is:-", my_copy_list)