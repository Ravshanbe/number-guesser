import random

def give_score(a, b):
    if a==1 and b==1:
        return 3, 3
    elif a==0 and b==0:
        return 1, 1
    elif a==1 and b==0:
        return 0, 5
    elif a==0 and b==1:
        return 5, 0

def bot1():
    return random.randint(0, 1)

def bot2(a):
    if a == 1:
        return 1
    else:
        return 0
    


finish = random.randint(16, 30)

count = 0

total_score_a = 0
total_score_b = 0
last_score_a = 1
while count < finish:
    a = int(input('Are you cooperating or not (press 1 or 0, respectively): '))
    b = bot1()
    last_score_a = a
    score_a, score_b = give_score(a, b)
    total_score_a += score_a
    total_score_b += score_b
    print(f"Bot's choice: {b}")
    print(f'Round {count+1}:\n {score_a} points to Damir aka | {score_b} points to Bot\n')
    print(f'Total score: \nDamir aka -- {total_score_a} points\nBot -- {total_score_b} points\n')

    count += 1

if total_score_a > total_score_b:
    print('Damir aka won!🎉')
elif total_score_a < total_score_b:
    print('Bot wins')
else:
    print('Draw')
