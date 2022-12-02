

def evaluate_play(hands):
	opponent = hands[0]
	player = hands[1]
	hand_score = 0
	play_score = 0

	possible_hands = ['A', 'B', 'C']

	opponent_index = possible_hands.index(opponent)

	match player:
		case 'X':
			player = possible_hands[(opponent_index - 1)%3]
			play_score += 0

		case 'Y':
			player = opponent
			play_score += 3
		case 'Z':
			player = possible_hands[(opponent_index + 1)%3]
			play_score += 6

	match player:
		case 'A':
			hand_score += 1
		case 'B':
			hand_score += 2
		case 'C':
			hand_score += 3

	

	return play_score + hand_score


def generate_plays():
	with open("input.txt") as file:
		data = file.read()
		hands = data.split('\n')
		total_score = 0
		for hand in hands:
			plays = hand.split(' ')
			score = evaluate_play(plays)
			total_score += score
	return total_score


def main():
	result = generate_plays()
	print(result)
  
  
	return 0

if __name__ == "__main__":
  main()