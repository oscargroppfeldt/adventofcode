

def eval(pairs):
	count = 0
	for group in pairs:
		elves = group.split(",")
		elf1 = elves[0]
		elf2 = elves[1]
		elf1_list = elf1.split("-")
		elf2_list = elf2.split("-")
		elf1_start = int(elf1_list[0])
		elf1_stop = int(elf1_list[1])
		elf2_start = int(elf2_list[0])
		elf2_stop = int(elf2_list[1])
		if (elf1_start >= elf2_start) and (elf1_start <= elf2_stop) and (elf1_stop <= elf2_stop) and (elf1_stop >= elf2_start):
			count += 1
		elif (elf2_start >= elf1_start) and (elf2_start <= elf1_stop) and (elf2_stop <= elf1_stop) and (elf2_stop >= elf1_start):
			count += 1
	return count


def main():
	with open("input.txt") as file:
		data = file.read()
		pairs = data.split("\n")
		res = eval(pairs)
		print(res)

  
  
	return 0

if __name__ == "__main__":
	main()