signal_color = input("Please enter Green, Yellow or Red color(Color's first letter in upper case):-")

if signal_color == "Red":
    print("Stop")
elif signal_color == "Green":
    print("Go")
elif signal_color == "Yellow":
    print("Look")
else:
    print("Entered color is not match for the traffic signal standards")