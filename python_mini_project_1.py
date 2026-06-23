import random

item_list = ["rock", "paper", "scissors"]

total_matches = int(input("How many matches do you want to play? "))

user_score = 0
comp_score = 0

for match in range(1, total_matches + 1):

    print(f"\n===== Match {match} =====")

    user_choice = input("Enter your move (rock, paper, scissors): ").lower()
    comp_choice = random.choice(item_list)

    print(f"Your Choice = {user_choice}")
    print(f"Computer Choice = {comp_choice}")

    if user_choice not in item_list:
        print("Invalid Input! Match Skipped.")
        continue

    if user_choice == comp_choice:
        print("Match Tie!")

    elif user_choice == "rock":
        if comp_choice == "paper":
            print("Paper covers Rock. Computer Wins!")
            comp_score += 1
        else:
            print("Rock smashes Scissors. You Win!")
            user_score += 1

    elif user_choice == "paper":
        if comp_choice == "scissors":
            print("Scissors cut Paper. Computer Wins!")
            comp_score += 1
        else:
            print("Paper covers Rock. You Win!")
            user_score += 1

    elif user_choice == "scissors":
        if comp_choice == "rock":
            print("Rock smashes Scissors. Computer Wins!")
            comp_score += 1
        else:
            print("Scissors cut Paper. You Win!")
            user_score += 1

    print(f"\nCurrent Score")
    print(f"You      : {user_score}")
    print(f"Computer : {comp_score}")

print("\n===== FINAL RESULT =====")
print(f"You      : {user_score}")
print(f"Computer : {comp_score}")

if user_score > comp_score:
    print("You Won The Set, You Brilliant!!")
elif comp_score > user_score:
    print("Computer Won The Set, You have to get Revenge Now!!")
else:
    print("The Set Ended In A Tie!!")