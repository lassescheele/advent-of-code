import pandas as pd

initial_memory = pd.read_csv("input.csv", sep=",", header=None).iloc[0,:].values

# Part 1
def run_intcode_program(noun, verb):
    memory = initial_memory.copy()
    memory[1:3] = [noun, verb]
    pointer_opcodes = [i for i in range(0,len(memory),4)]
    for pointer_opcode in pointer_opcodes:
        opcode = memory[pointer_opcode]
        if opcode == 99:
            break
        elif opcode == 1:
            memory[memory[pointer_opcode+3]] = memory[memory[pointer_opcode+1]] + memory[memory[pointer_opcode+2]]
        elif opcode == 2:
            memory[memory[pointer_opcode+3]] = memory[memory[pointer_opcode+1]] * memory[memory[pointer_opcode+2]]
    return(memory[0])
print("Part 1: ",run_intcode_program(12, 2))

# Part 2
find = False
for noun in range(0,100):
    for verb in range(0,100):
        if run_intcode_program(noun, verb) == 19690720:
            find = True 
            break
    if find: 
        break
print("Part 2: ",100 * noun + verb)