while True:
  print("""
  1.Addition
  2.Subtraction
  3.Multiplication
  4.Divide
  5.Exit
  """)
  Choice = input("Enter your choice: ")
  if Choice == '1':
    Num1 = int(input("Enter 1st number: "))
    Num2 = int(input("Enter 2nd number: "))
    print("Addition is:",Num1+Num2)
  elif Choice == '2':
    Num1 = int(input("Enter 1st number: "))
    Num2 = int(input("Enter 2nd number: "))
    print("Subtraction is:",Num1-Num2)
  elif Choice == '3':
    Num1 = int(input("Enter 1st number: "))
    Num2 = int(input("Enter 2nd number: "))
    print("Multiplication is:",Num1*Num2)
  elif Choice == '4':
    Num1 = float(input("Enter 1st number: "))
    Num2 = float(input("Enter 2nd number: "))
    print("Divide is:",Num1/Num2)
  elif Choice == '5':
    break
  else:
    print("Invalid choice")