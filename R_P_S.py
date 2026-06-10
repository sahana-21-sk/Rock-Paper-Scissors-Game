import random
options = ['r', 'p', 's']
while True:
    comp_choice = random.choice(options)
    user_choice = input("Rock, Paper or scissors? (r/p/s) or 'q' to quit: ").lower()
    if user_choice == 'q':
        print("Thanks for playing!")
        break  
    if user_choice not in options:
        print("Invalid choice! Please type r, p, or s.")
        continue
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {comp_choice}")
    if user_choice == comp_choice:
        print("It's a tie!")
    elif (user_choice == 'r' and comp_choice == 's') or \
         (user_choice == 'p' and comp_choice == 'r') or \
         (user_choice == 's' and comp_choice == 'p'):
        print("You win!! 🎉")
    else:
        print("Computer wins! 🤖")
    print("-" * 20)


