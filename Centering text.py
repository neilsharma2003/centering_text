import math
width = int(input())
my_inputs = []
while True:
    temp = input()
    my_inputs.append(temp)
    if temp == "END":
        break
my_inputs.pop()
for i in my_inputs:
    num_of_dots = width - len(i)
    numdots_right = math.floor(num_of_dots/2)
    numdots_left = math.ceil(num_of_dots/2)
    print("."*numdots_left + i + "."*numdots_right)

    
    

