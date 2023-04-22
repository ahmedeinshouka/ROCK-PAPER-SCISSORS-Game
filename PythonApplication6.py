import random 
print("**************************************************************")
print("ROCK PAPER SCISSORS Game")
print("**************************************************************")
choice=int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors."))
print("**************************************************************")
print("your choice:")
if choice==0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif choice==1:
     print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif choice ==2:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print(" please check your choice again !!!")
computer_choice=random.randint(0,2)
print("*******************************************************************")
print("your computer choice:")
if computer_choice==0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif computer_choice==1:
     print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif computer_choice ==2:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
print("*******************************************************************************************************")
if computer_choice==0 and choice==2:
    print("You lose")
elif computer_choice==0 and choice==1:

    print("You win")
elif computer_choice==0 and choice==0:
    print("Drawing")
elif computer_choice==1 and choice==1:
    print("Drawing")
elif computer_choice==1 and choice==0:
    print("You lose")

elif computer_choice==1 and choice==2:
    print("You win")
elif computer_choice==2 and choice==2:
    print("Drawing")
elif computer_choice==2 and choice==0:
    print("You win")
elif computer_choice==2 and choice==1:
    print("You lose")
print("**************************************************************************************************************")



