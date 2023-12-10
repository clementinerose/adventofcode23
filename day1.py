import numpy as np


def part1():
  with open("input1.txt") as file:
    sum = []
    Lines = file.readlines()
    for line in Lines:
      first, last = 0, 0
      bool = False
      for char in line:
        if char.isnumeric():
          if bool is False:
            first = char
            bool = True
          last = char
      sum.append(int(str(first) + str(last)))
    print(np.sum(sum))


def part2(yo):
  with open(yo) as file:
    sum = []
    numm = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    ]
    Lines = file.readlines()
    for line in Lines:
      first, last = 0, 0
      found_First = False
      for num_in_line in range(len(line)):
        if line[num_in_line].isnumeric():
          if found_First is False:
            first = line[num_in_line]
            found_First = True
          else: 
            last = line[num_in_line]
        else: 
          for z in range(len(numm)):
            num = numm[z]
            counter = 0
            for k in range(len(num)): 
              letter_from_array = num[k]
              if len(line) <= (num_in_line + k):
                break
              else: 
                letter_from_text = line[num_in_line + k] 
              if letter_from_array == letter_from_text:
                counter += 1
                if counter == len(num):
                  if found_First is False:
                    first = z +1
                    found_First = True
                    break  
                  else:
                    last = z +1    
      sum.append(int(str(int(first)) + str(int(last))))
    print(np.sum(sum))


part1()
part2("test1.txt")