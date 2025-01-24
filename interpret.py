with open("main.txt", "r") as f:
  data = f.readlines()
  memory = [0]*int(data[0][1:])
