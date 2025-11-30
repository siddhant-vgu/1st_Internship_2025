Age = int(input("Enter your Age: "))
if(Age>18):
  print("Congrates your are allow to watch ADULT movie")
  if(Age>18):
    Id = str(input("if you have ticket press 'Y' else 'N': "))
    if (Id == 'Y'):
      print("Congrate, Enjoy your movie.")
    elif (Id == 'N'):
      print("thanks for being honest")
elif(Age>=15):
  print("You are allow to see PG-13 movie")
else:
  print("You are not allow to watch any movie")