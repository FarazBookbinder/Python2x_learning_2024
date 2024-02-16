
#Another 1
text = "Faraz"
reversed_text = ""
for i in text:
    reversed_text = i + reversed_text

print(reversed_text)

#approach 2
def reverse_str(text):
    reversed_text = ""
    for i in text:
        reversed_text = i + reversed_text
    return reversed_text

name = reverse_str("Faraz")
print(name)