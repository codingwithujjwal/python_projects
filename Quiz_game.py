print("welcome to my computer quiz!")

playing=input("Do you want to play?\n")

if playing.lower() !="yes":
    quit()

print("Okey! Let's play:")
#score=0

answer=input("what does cpu stand for?\n")
if answer.lower()=="central processing unit":
    print("correct")
    score+=1
else:
    print("Incorrect")
    
answer=input("what does gpu stand for?\n")
if answer.lower()=="graphics processing unit":
    print("correct")
    score+=1
else:
    print("Incorrect")  
    
answer=input("what does RAM stand for?\n")
if answer.lower()=="random access memory":
    print("correct")
    score+=1
else:
    print("Incorrect")    
    
answer=input("what does PSU stand for?\n")
if answer.lower()=="power supply":
    print("correct")
    score+=1 
else:
    print("Incorrect")    
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")