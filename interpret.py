with open("main.txt", "r") as f:
  data = f.readlines()
  if data[0][0] == "!":
    memory = [0]*int(data[0][1:])
    print(memory)
    run = True
  else:
    print("Error, initialiser (!) was not found")
