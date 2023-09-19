import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_choices = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissor!")
choice = input("What do you choose? 'rock', 'paper' or 'scissor'? ")

computer_choice = random.randint(0, 2)

cpu_choice = list_choices[computer_choice]

if choice == "rock":
    print(rock)
    print(cpu_choice)
    if cpu_choice == scissors:
        print("You win!")
    elif cpu_choice == rock:
        print("It's a draw!")
    else: 
        print("You lose!")
elif choice == "paper":
    print(paper)
    print(cpu_choice)
    if cpu_choice == rock:
        print("You win!")
    elif cpu_choice == paper:
        print("It's a draw!")
    else: 
        print("You lose!")
elif choice == "scissors":
    print(scissors)
    print(cpu_choice)
    if cpu_choice == paper:
        print("You win!")
    elif cpu_choice == scissors:
        print("It's a draw!")
    else: 
        print("You lose!")