import random
def passwordgenerator():
    lowerChars = ["a","b","c","d","e"]
    upperChars = ["A","B","C","D","E"]
    specialChars = ["#","*","&","@"]
    numericChars = ["1","2","3","4","5"]
    password = random.choice(lowerChars) + random.choice(upperChars) + random.choice(specialChars) +random.choice(numericChars)
    password = password + password + password + password
    return password
