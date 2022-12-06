

def generate_stacks(crates):
	rows = crates.split("\n")
	stacks = [[] for _ in range(len(rows[-1].split()))]
	rows = rows[:-1] #Remove numbering row

	for i in reversed(range(len(rows))):
		row = rows[i]
		index = 0
		stack = 0
		whitespace_counter = 0
		while index < len(row):
			if row[index] == " ":
				if whitespace_counter == 3:
					stack += 1
					whitespace_counter = 0
					index += 1
				else:
					whitespace_counter += 1
					index += 1
			else:
				stacks[stack].append(row[index] + row[index + 1] + row[index + 2])
				index += 3
				whitespace_counter = 0
				stack += 1
	return stacks



def generate_moves(instr):
	resulting_instr = []
	instr_list = instr.split("\n")
	for move in instr_list:
		split_move = move.split(" ")
		resulting_instr.append([split_move[1], split_move[3], split_move[5]])

	return resulting_instr

def preform_moves(stacks, moves):

	for move in moves:
		popped_elements = []
		for _ in range(int(move[0])):
			popped_elements.append(stacks[int(move[1]) - 1].pop())
		popped_elements.reverse()
		for element in popped_elements:
			stacks[int(move[2]) - 1].append(element)
	
	res_string = ""
	for stack in stacks:
		res_string += stack[-1][1]
	return res_string

def main():
	with open("input.txt") as file:
		data = file.read()
		split = data.split("\n\n")
		crates = split[0]
		instructions = split[1]
		stacks = generate_stacks(crates)
		moves = generate_moves(instructions)
		result = preform_moves(stacks, moves)
		print(result)
  
  
	return 0

if __name__ == "__main__":
	main()