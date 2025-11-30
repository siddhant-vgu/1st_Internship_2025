# user_input = input("Enter your sentence:")

# abusive_word = ["stupid","idiot","mc","bc","chutiya","bsdk"]

# splited_input_list = user_input.split()

while True:
  print("1.Add abusive word in file \n2.Text filter \n3.Abusive word list \n4.Remove Element \n5.Exit\n")
  choice = input("Enter your choice: ")


  if choice == "1":
    New_Word = input("Enter New word to add file: ")
    with open("Day3\Abuses.txt","a") as f:
      f.write(New_Word.lower() + "\n")
    print("Added successfully...\n")


  elif choice == "2":
    user_input = input("Enter your sentence:")
    splited_input_list = user_input.split()
    with open("Day3\Abuses.txt","r") as f:
      abusive_word = [i.strip() for i in f.readlines()]
    try:
      for i in abusive_word:
        if i in splited_input_list:
          user_input = user_input.replace(i,"***")
      print("\nfiltered data is:\n" ,user_input ,"\n")
    except:
      print("Error in loops")


  elif choice == "3":
    with open("Day3\Abuses.txt", "r") as f:
      words = [i.strip() for i in f.readlines()]
    print("abusive words in list: ", words,"\n")


  elif choice == "4":
    word = input("Which word u want to delete: ").lower()
    with open("Day3\Abuses.txt","r") as f:
      abusive_word = [i.strip() for i in f.readlines()]
    if word in abusive_word:
      abusive_word.remove(word)
      print(f"{word} removed succesfully\n")
    else:
      print(f"{word} not found\n")


  elif choice == "5":
    print("Exiting...")
    break


  else:
    print("\nInvalid input. \nPlease input one of them...\n")