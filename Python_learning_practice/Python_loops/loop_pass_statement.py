# pass is null statement that does nothing. it is use as placeholder for the future code.
# Below is the examples why need the pass statement.
# for i in range(4):
# #   (Wihtout pass is move to next line?)
# print("No without pass statement is not move to next because the loop is incomplete for thr interpreter.")
# Above is wrong
#Below is right

for i in range(10):
    pass
print("Interpreter move this line")