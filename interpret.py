def interpret(file):
  with open(file, "r") as f:
    data = f.readlines()
    if data[0][0] == "!":
      memory = [0]*int(data[0][1:])
      pointer = 0
      print(memory)
      run = True
    else:
      print("Error, initialiser (!) was not found")
      exit()
  
    for line in data:
      line = line.split()
      if line[0] == "SET":
        print("Sett")

interpret("main.txt")