import streamlit as st
import random
import time

# Function to generate a random number based on difficulty
def generate_random_number(difficulty):
    if difficulty == "Easy":
        return random.randint(1, 10)
    elif difficulty == "Medium":
        return random.randint(1, 50)
    elif difficulty == "Hard":
        return random.randint(1, 100)

# Streamlit app
st.title('🎯 Advanced Number Guessing Game 🎯')

# Difficulty selector with emojis
difficulty = st.selectbox("Select Difficulty", ["Easy 🟢", "Medium 🟡", "Hard 🔴"])

# Start the game button
if 'started' not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    st.session_state.number = generate_random_number(difficulty.split()[0])  # Extract difficulty level without emoji
    st.session_state.attempts = 0
    st.session_state.history = []
    st.session_state.start_time = None

# Timer setup
if st.session_state.started and st.session_state.start_time is None:
    st.session_state.start_time = time.time()

# Game start
if st.button("🎮 Start New Game"):
    st.session_state.started = True
    st.session_state.number = generate_random_number(difficulty.split()[0])
    st.session_state.attempts = 0
    st.session_state.history = []
    st.session_state.start_time = time.time()

# User input for guessing the number
if st.session_state.started:
    user_guess = st.number_input("Guess a number:", min_value=1, step=1)

    # Submit guess button
    if st.button("Submit Guess"):
        if user_guess < st.session_state.number:
            st.session_state.attempts += 1
            st.session_state.history.append(f"Attempt {st.session_state.attempts}: {user_guess} (🔻 Too Low)")
            st.write(f"Attempt {st.session_state.attempts}: 🔻 Too low! Try again.")
        elif user_guess > st.session_state.number:
            st.session_state.attempts += 1
            st.session_state.history.append(f"Attempt {st.session_state.attempts}: {user_guess} (🔺 Too High)")
            st.write(f"Attempt {st.session_state.attempts}: 🔺 Too high! Try again.")
        else:
            st.session_state.attempts += 1
            elapsed_time = round(time.time() - st.session_state.start_time, 2)
            st.session_state.history.append(f"Attempt {st.session_state.attempts}: {user_guess} (🎉 Correct!)")
            st.write(f"🎉 Congratulations! You've guessed the number {st.session_state.number} correctly!")
            st.write(f"It took you {st.session_state.attempts} attempts and {elapsed_time} seconds.")

            # Show history of attempts
            st.write("🔄 History of Attempts:")
            for record in st.session_state.history:
                st.write(record)

            # End the game and show stats
            st.write(f"✅ Total attempts: {st.session_state.attempts}")
            st.write(f"⏱️ Total time taken: {elapsed_time} seconds")

            # Game Reset
            st.session_state.started = False

    # Display history of guesses with emojis
    st.write("📝 History of Guesses:")
    for record in st.session_state.history:
        st.write(record)

