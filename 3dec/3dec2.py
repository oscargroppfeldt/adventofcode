
def get_group_badge_score(elf1, elf2, elf3):
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for letter1 in elf1:
		for letter2 in elf2:
			if letter1 == letter2:
				for letter3 in elf3:
					if letter3 == letter1:
						return (alphabet.index(letter1) + 1)

def generate_elf_group():
	result = 0
	with open("input.txt") as file:
		data = file.read()
		rucksacks = data.split('\n')
		for index in range(len(rucksacks)//3):
			result += get_group_badge_score(rucksacks[3*index], rucksacks[3*index + 1], rucksacks[3*index + 2])

		

	return result


def main():

	res = generate_elf_group()
	print(res)
  
	return 0

if __name__ == "__main__":
		main()