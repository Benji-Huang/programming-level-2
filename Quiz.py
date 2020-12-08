# Quiz Game
# Author: Benjamin Huang
# Date: Dec. 4, 2020

# Initialize score
score = 0

# Ask first question
ans_one = input("Hello! Welcome to my quiz game.\nAre you cool?[Y/N]\n").upper()

# Respond accordingly, add score after if needed
if ans_one == "Y":
    print("Okay, yea your pretty cool. Here's a point")
    score += 1
elif ans_one == "N":
    print("Nah I think your cool, though. But here's a pity point")
    score += 1
else:
    print("I have no clue what you said. You get nothing")

# Ask second question
ans_two = input("Let's see if you're good at math. What is 6 * (4 - 2) / 2^2\n").lower()

# Respond accordingly, add score after if needed
if ans_two == "3" or ans_two == "three":
    print("Nice, thanks for doing my math homework. I'll give you a point in return")
    score += 1
else:
    print("Hmmmmm, I'm not too sure about that one. The answer key has a different answer. Maybe you should stick to programming.")

# Ask third question
ans_three = input("Now, let's see if you payed attention during science class\nWhat is the sixth planet furthest from the Sun?\n").lower()

# Respond accordingly, add score after if needed
if ans_three == "saturn":
    print("Sweeeeet. Maybe that was too easy for you!")
    score += 1
else:
    print(f"Are you sure it's {ans_three}?")

# Ask fourth question
ans_four = input("History time! What year was Canada established?\n").lower()

# Respond accordingly, add score after if needed
if ans_four == "1867" or ans_four == "eighteen sixty seven":
    print("Nope, that ain't it... haha I'm joking. Yea you're right.")
    score += 1
else:
    print("I'm disappointed.")

# Ask fifth question
ans_five = input("Last question! What is the FitnessGram Pacer Test? Is it\nA)Some exercise\nB)IDK\nC)The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly but gets faster each minute after you hear this signal bodeboop. A sing lap should be completed every time you hear this sound. ding Remember to run in a straight line and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark. Get ready!… Start.\n").upper()

# Respond accordingly, add score after if needed
if ans_five == "C":
    print("Good, you're cultured")
    score += 1
else:
    print("Nooope, now do 10 push-ups")

# Display final score
print(f"Your final score is {score / 5 * 100} %")