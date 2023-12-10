import numpy as np

def part1():
  with open("test2.txt") as file:
    colours = {
      "blue": 14,
      "red": 12,
      "green": 13,
    }
    sum = list(range(1,6))
    print(sum)
    Lines = file.readlines()
    for line in Lines:
      line = line.strip().replace(" ","")
      Game = line[4] 
      k = 5
      if line[5].isnumeric(): 
        Game = int(str(line[4]) + str(line[5]))
        k = 6
    
      elif line[5].isnumeric() and line[6].isnumeric(): 
        Game = int(str(line[4]) + str(line[5]) + str(line[6]))
        k = 7
      number = 0
      found_number = False

      for i in range(k, len(line)-2):
        if line[i].isnumeric() and found_number is False: 
          number = line[i]
          found_number = True
        if line[i + 1].isnumeric() and line[i].isnumeric():
          number = int(str(line[i]) + str(line[i+1]))
          found_number = True 
        
        if line[i].isalpha():
          if line[i:i+3] == "red":
            if int(number) > int(colours["red"]):
              sum[int(Game)-1] = 0
              found_number = False
              break 
          elif line[i:i+4] == "blue":
            if int(number) > int(colours["blue"]):
              sum[int(Game)-1] = 0
              found_number = False
              break 
          elif line[i:i+5] == "green" and int(number) > colours["green"]:
              sum[int(Game)-1] = 0
              found_number = False

    print(np.sum(sum))
      
part1()
