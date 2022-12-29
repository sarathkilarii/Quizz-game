print("Welcome to quizz game")

playing = input("Do you want to play game: ")
score = 0

if playing.lower() != "yes":
    quit()

print("lets play :) ")

answer_1= input("what is india capital")
if answer_1.lower() == "delhi":
    print("correct")
    score += 1
else:
    print("incorrect")
answer_2 = input("what is Germany capital")
if answer_2.lower() == "berlin":
    print("correct")
    score +=1
else:
    print("incorrect")
answer_3 = input("what is spain capital")
if answer_3.lower() == "madrid":
        print("correct")
        score +=1
else:
    print("incorrect")
answer_4 = input("what is netherland's capital")
if answer_4.lower() == "amsterdam":
     print("correct")
     score +=1
else:
     print("incorrect")

print("your score is"+ str(score))
print("your score is"+ str((score/4)*100)+"%" )

