import math
def reverse_str(text):
    reversed_text = ""
    for i in text:
        reversed_text = i + reversed_text
    return reversed_text
original_text = input("Please enter text"
original_text = original_text.lower()
reversed_text = reverse_str(original_text)
print(reversed_text)

## Pending need to understand first then do it