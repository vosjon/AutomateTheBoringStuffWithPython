import random

def getAnswer(answeredNumber):
    if answeredNumber == 1:
        return "It is certain"
    elif answeredNumber == 2:
        return "It is decidedly so"
    elif answeredNumber == 3:
        return "Yes"
    elif answeredNumber == 4:
        return "Reply hazy try again"
    elif answeredNumber == 5:
        return "Ask again later"
    elif answeredNumber == 6:
        return "Concentrate and ask again"
    elif answeredNumber == 7:
        return "My reply is no"
    elif answeredNumber == 8:
        return "Outlook not so good"
    elif answeredNumber == 9:
        return "Very doubtful"
    

print(getAnswer(random.randint(1, 9)))