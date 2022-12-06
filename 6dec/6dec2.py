
def unique_string(string):
	return (len(set(string)) == len(string))


def find_marker(string):
	found = False
	working_string = string[:14]
	index = 1
	while not found:
		if unique_string(working_string):
			found = True
		else:
			working_string = working_string[1:]
			working_string += string[index]
			index += 1
	return index




def main():
	with open("input.txt") as file:
		data = file.read()
		marker_index = find_marker(data)
		print(marker_index)
  
	return 0

if __name__ == "__main__":
	main()