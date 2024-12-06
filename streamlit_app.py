import random
import streamlit as st

# Function to start the game
def number_guess():
    # Set up the game state
    if "number" not in st.session_state:
        st.session_state.number = random.randint(1, 101)
    if "message" not in st.session_state:
        st.session_state.message = "Welcome! Try to guess the number between 1 and 100."
    if "guess" not in st.session_state:
        st.session_state.guess = None
    if "game_over" not in st.session_state:
        st.session_state.game_over = False

    # Show game instructions or game over message
    st.title("Guess the Number Game!")
    st.write(st.session_state.message)

    # Input field for the guess
    if not st.session_state.game_over:
        guess_input = st.text_input("Enter your guess (or 'q' to quit):", key="guess_input")
        submit_button = st.button("Submit Guess")

        if submit_button:
            if guess_input.lower() == 'q':
                st.session_state.message = "You have quit the game. Thanks for playing!"
                st.session_state.game_over = True
            else:
                try:
                    guess = int(guess_input)
                    if guess == st.session_state.number:
                        st.session_state.message = "You guessed it right!"
                        st.session_state.game_over = True
                    elif guess < st.session_state.number:
                        st.session_state.message = "Not right! You guessed too small."
                    else:
                        st.session_state.message = "Not right! You guessed too high."
                except ValueError:
                    st.session_state.message = "Please enter a valid number."
    else:
        # If the game is over, show a restart button
        restart_button = st.button("Restart Game")
        if restart_button:
            st.session_state.clear()
            number_guess()

# Start the game
number_guess()
