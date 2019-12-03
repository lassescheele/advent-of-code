import math as m
import pandas as pd

intcode_df = pd.read_csv("input.csv", sep=",", header=None)
intcode_array = intcode_df.iloc[0,:].values

# Part 1
def run_computer(array):
    index_opcodes_list = [i for i in range(0,len(array),4)]
    for index_opcode in index_opcodes_list:
        opcode = array[index_opcode]
        if opcode == 99:
            break
        elif opcode == 1:
            array[array[index_opcode+3]] = array[array[index_opcode+1]] + array[array[index_opcode+2]]
        elif opcode == 2:
            array[array[index_opcode+3]] = array[array[index_opcode+1]] * array[array[index_opcode+2]]
    return(array)

intcode_array_part1 = intcode_array.copy()
intcode_array_part1[1:3] = [12,2]
print("Part 1: ",run_computer(intcode_array_part1)[0])

# Part 2
goal = 19690720
find = False
for noun in range(0,99):
    print(noun)
    for verb in range(0,99):
        intcode_array_part1 = intcode_array.copy()
        intcode_array_part1[1:3] = [noun,verb]
        result = run_computer(intcode_array_part1)[0]
        if result == goal:
            print(noun, verb, result)
            find = True 
            break
    if find: 
        break
print("Part 2: ",100 * noun + verb)