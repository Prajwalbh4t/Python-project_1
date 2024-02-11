print("Hello, Welcome to my Great indian Quiz!")

playing = input("Are you ready to play the Great Indian Quiz Game?! Y? N? ")

if playing != "Y":
    exit()

print("-----------------------------------------------------")
print("So then Let's Go!!!  Here's your first question: ")
score = 0

answer_one = input("\n 1) Which city is called the 'Garden city of India'? ").lower()
if answer_one == "bengaluru":
    print("you answer is correct!!, onto your next question now....")
    score += 1
else:
    print("Sorry, your answer is wrong")



answer_two = input("\n 2) Bhubhaneshwar is the capital of? ").lower()
if answer_two == "odisha":
    print("you answer is correct!!, onto your next question now....")
    score += 1
else:
    print("Sorry, your answer is wrong")


answer_three = input("\n 3) National flower of india? ").lower()
if answer_three == "lotus":
    print("you answer is correct!!, onto your next question now....")
    score += 1
else:
    print("Sorry, your answer is wrong")


answer_four = input("\n 4) where is eden garden stadium located? ").lower()
if answer_four == "kolkota":
    print("you answer is correct!!, onto your next question now....")
    score += 1
else:
    print("Sorry, your answer is wrong")


answer_five = input("\n 5) which IPL team Virat kohli plays for? ").lower()
if answer_five == "rcb":
    print("you answer is correct!!")
    score += 1
else:
    print("Sorry, your answer is wrong")

print("\n ----------Thanks for participating in our Great Indian Quiz!----------")
print("\n Your High score is: " + str(score))
print("\n You got " + str(score/5 *100) + "%")