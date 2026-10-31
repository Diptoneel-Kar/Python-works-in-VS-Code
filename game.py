import random

secret_number = random.randint(1, 10)
print("--- 🎲 Number Guessing Game 🎲 ---")
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("🏆 Spot on! You won!")
else:
    print(f"❌ Close! The number was {secret_number}.")
