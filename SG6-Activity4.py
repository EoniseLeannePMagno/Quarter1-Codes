name = input("Enter your full name (First Name, Middle Name, Last Name): ")
first, middle, last = [n.strip().capitalize() for n in name.split(",")]
middle_initial = middle[0].upper() + "."
formatted_name = f"{last}, {first} {middle_initial}"
print("Formatted Name:", formatted_name)