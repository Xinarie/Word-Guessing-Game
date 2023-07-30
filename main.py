import random

def select_random_word():
	words = ['python', 'programming', 'computer', 'algorithm', 'variable']
	return random.choice(words)

def display_word(word, guessed_letters):
	display = ""
	for letter in word:
		if letter in guessed_letters:
			display += letter
		else:
			display += "_"
	return display

def main():
	print("Welcome to the Word Guessing game!")
	play_again = True

	while play_again:
		selected_word = select_random_word()
		guessed_letters = []
		max_attempts = 6
		attempts = 0

		while True:
			display = display_word(selected_word, guessed_letters)
			print("Predicted word: ", display)

			if display == selected_word:
				print("Congratulations, you've won!")
				break

			if attempts >= max_attempts:
				print("You have no right to guess. The right word: ", selected_word)
				break

			guess = input("Guess a letter: ").lower()

			if len(guess) != 1 or not guess.isalpha():
				print("Invalid input. Enter a letter.")
				continue

			if guess in guessed_letters:
				print("You have already guessed this letter.")
				continue

			guessed_letters.append(guess)

			if guess not in selected_word:
				attempts += 1
				print(f"{guess} letter is incorrect. You have {max_attempts - attempts} guesses left.")

		play_again = input("Want to play a new game? (Press 'y' for Yes): ").lower() == 'y'

if __name__ == "__main__":
	main()