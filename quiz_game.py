print("Welcome to my Computer Quiz ! ")
playing = input("Do You want to play ?\n ")
print(playing)

if playing != "yes":
    print("ok Then we will see later")
    quit()
else:
    print("Lets have a  Quick Match !\n")
    
score = 0

answer = input("What is RAM ?\n").lower()
if answer == "random access memory":
    print("Nice ! Your answer is Correct")
    score += 1
else:
    print("Wrong answer Better Luck Next Time!\n")
    
answer = input("what is CPU ?\n").lower()
if answer == "computer":
    print("Nice ! Your answer is Correct")
    score += 1
else:
    print("Wrong answer Better Luck Next Time!\n")
    
answer = input("what is CU ?\n").lower()
if answer == "control unit":
    print("Nice ! Your answer is Correct")
    score += 1
else:
    print("Wrong answer Better Luck Next Time!\n")
    
answer = input("what is G.O.A.T ?\n").lower()
if answer == "nice time":
    print("Nice ! Your answer is Correct")
    score += 1
else:
    print("Wrong answer Better Luck Next Time!\n")
    
print("Your score " + str( score )+ " in this quiz !")
print("Your Quiz Percentage is " + str(( score/4*100 )) + " in this match !")
    
    