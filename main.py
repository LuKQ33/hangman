import random
import hangman_words
import hangman_art

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

game_over = False
correct_letters = []
incorrect_letters = []
display = placeholder
while not game_over:
    print(f"****************************<{lives}/6 LIVES LEFT****************************")
    print(hangman_art.stages[lives])
    print("Word to guess: " + display) # (Nota: asegúrate de inicializar display antes o mostrarlo ordenado)
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            break
        print("⚠️ Entrada inválida. Por favor, ingresa una sola letra.")
    # 1. Primero mostramos las vidas y el dibujo al comenzar el turno



    # 2. Validamos letras repetidas
    if guess in incorrect_letters or guess in correct_letters:
        print(f"You've already guessed {guess}.")
        continue # Salta al siguiente turno para no procesar dos veces

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    # 3. Validamos si falló
    if guess not in chosen_word:
        lives -= 1
        incorrect_letters.append(guess)
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************\nThe correct word was {chosen_word.upper()}")
            print(hangman_art.stages[lives]) # Muestra el ahorcado completo al perder

    # 4. Validamos si ganó
    if "_" not in display:
        game_over = True
        print(f"{chosen_word.upper()}")
        print("****************************YOU WIN****************************")
    if incorrect_letters:
        print(f"These are the incorrect guesses: {set(incorrect_letters)}")