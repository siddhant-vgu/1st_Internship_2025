balance = 50000
pin = 1234

count = 0

while count < 5:
  user_pin = int(input("Enter your pin: "))
  if user_pin == pin:
    print(f"Your balance is: {balance}")
    amount = int(input("Enter the amount to withdraw: "))
    if amount > balance:
      print(f"You have not sufficient balance\nYour balance is:{balance}\nYour entered amount is:{amount}")
    else:
      print(f"Withdraw {amount} successfully.")
      balance -= amount
      print(f"Your balance is: {balance}")
    break
  else:
    print("Invalid pin")
    count+=1
    if count==3:
      print(f"Now you have only {5-count} changes ")
    elif count==5:
      print(f"Your pin is locked due to {count} times wrong attempt")