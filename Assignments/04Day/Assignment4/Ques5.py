user_string = input("Enter a string: ")

unique_chars = []

for ch in list(user_string):
    if ch not in unique_chars:
        unique_chars.append(ch)

print("Unique characters:", unique_chars)