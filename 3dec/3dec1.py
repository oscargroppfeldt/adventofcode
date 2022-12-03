
def get_rucksack_score(comp1, comp2):
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	overlapping_item = ""
	for letter1 in comp1:
		for letter2 in comp2:
			if letter1 == letter2:
				overlapping_item = letter1
				return alphabet.index(overlapping_item) + 1




def generate_rucksack_contents():
	result = 0
	with open("input.txt") as file:
		data = file.read()
		rucksacks = data.split('\n')
		for rucksack in rucksacks:
			content_length = len(rucksack)
			comp1 = rucksack[0:content_length//2]
			comp2 = rucksack[content_length//2:]
			result += get_rucksack_score(comp1, comp2)

	return result


def main():

	res = generate_rucksack_contents()
	print(res)
  
	return 0

if __name__ == "__main__":
		main()