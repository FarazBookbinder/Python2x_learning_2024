# Break and Continue

# Break - loop is stop and terminate
# like as below
# i = 1
# while i <= 5:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# Continue - It means further code is skip and continue with the same code again
# like as below

i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
