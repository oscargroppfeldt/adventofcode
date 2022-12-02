

def evaluate_play(hands):
	opponenet = hands[0]
	player = hands[1]
	hand_score = 0

	possible_hands = ['A', 'B', 'C']

	match player:
		case 'X':
			player = 'A'
			hand_score += 1
		case 'Y':
			player = 'B'
			hand_score += 2
		case 'Z':
			player = 'C'
			hand_score += 3

	player_index = possible_hands.index(player)
	opponent_index = possible_hands.index(opponenet)

	play_score = 0
	if (player_index - 1)%3 == opponent_index:
		play_score += 6
	elif player_index == opponent_index:
		play_score += 3
	elif (opponent_index - 1)%3 == player_index:
		play_score += 0
	

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