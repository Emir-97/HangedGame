import time
name = input("What's your name?")
print("Hello, ",name," it's time to play!!")
print(" ")
time.sleep(1)
print("Start guessing")
time.sleep(0.5)
word = "sexi"
yourWord =" "
lifes = 5

while lifes>0:
  fails=0
  for letter in word:
    if letter in yourWord:
       print(letter,end="")
    else:
       print("*",end="")
       fails+=1
  if fails==0:
    print("")
    print("Congratulations your won")
    break

  yourLetter=input(" Enter your letter")
  yourWord+=yourLetter

  if yourLetter not in word:
    lifes-=1
    print("Wrong")
    print("You have got ",lifes," lifes")
  if lifes == 0:
    print("End Game")
else:
 print("")
 print("Thanks for participating")
