"""number guessing game
2 input players
age > 12 --play
age < 12--exit
mode of game-- easy(1,10), medium(1,30), hard(1,50)
10 rounds
p1--scores 1 point add 1
p2--scores 0 point add 0
p1 and p2 scored same--game draw
count total scores _/10
if p1 wins-- prompt msg
else-- p2 wins."""
import random
p1_age = int(input("Enter Player 1's age: "))
p2_age = int(input("Enter Player 2's age: "))

if p1_age > 12 or p2_age > 12:
    p1=input("enter player 1 name: ")
    p2=input("enter player 2 name: ")
    print("Choose game mode: ")
    print("1. Easy (Range: 1-10)")
    print("2. Medium (Range: 1-30)")
    print("3. Hard (Range: 1-50)")
    mode = int(input("Enter your choice (1/2/3): "))

    if mode == 1:
        range_start, range_end = 1, 10
    elif mode == 2:
        range_start, range_end = 1, 30
    elif mode == 3:
        range_start, range_end = 1, 50
    else:
        print("Invalid choice. Defaulting to Easy mode.")
    print("choose rounds: ")
    print("3. for 3 rounds")
    print("5 for 5 rounds")
    print("10 for 10 rounds")
    rounds=int(input("enter rounds(3/5/10): "))
    if rounds==3:
        range_start, range_end = 1, 10
    elif rounds==5:
        range_start, range_end = 1, 30
    else:
        range_start, range_end = 1, 50


    p1_score = 0
    p2_score = 0

    for round_num in range(rounds):
        print(f"\nRound {round_num}")

        secret_number = random.randint(range_start, range_end)

        print(f"{p1}'s turn:")
        p1_guess = int(input(f"Guess a number between {range_start} and {range_end}: "))
        print(f"{p2}'s turn:")
        p2_guess = int(input(f"Guess a number between {range_start} and {range_end}: "))

        if secret_number == p1_guess:
            print(f"{p1} scores a point!")
            p1_score += 1
        elif secret_number > p1_guess:
            print("too low")
        elif secret_number < p1_guess:
            print("too high")
        elif secret_number == p2_guess:
            print(f"{p2} scores a point!")
            p2_score += 1
        elif secret_number > p2_guess:
            print("too low")
        elif secret_number < p2_guess:
            print("too high")
        else:
            print("It's a draw! No points this round.")

        print(f"The secret number was: {secret_number}")
        print(f"Scores after Round {round_num} - {p1}: {p1_score}, {p2}: {p2_score}")

    print("\nGame Over!")
    print(f"Final Scores - {p1}: {p1_score}, {p2}: {p2_score}")

    if p1_score > p2_score:
        print(f"{p1} wins the game! Congratulations!")
    elif p2_score > p1_score:
        print(f"{p2} wins the game! Congratulations!")
    else:
        print("The game is a draw! Well played both!")

else:
    print("Both players must be above 12 years old to play the game.")
