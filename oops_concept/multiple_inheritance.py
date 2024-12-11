class A:
    vara = "This is my class A"


class B:
    varb = "This is my class B"


class C(A, B):
    varc = "This is the child of class A and Class B"

createobj = C
print(createobj.varc)
print(createobj.vara)
print(createobj.varb)