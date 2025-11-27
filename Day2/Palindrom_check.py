word = input("Enter your value to check palindrom: ")
reversed = word[::-1]
if word == reversed:
  print(f"Yes,{word} is Palindrom.")
else:
  print("Not palindrom")
