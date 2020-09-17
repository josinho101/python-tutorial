import sys
import random

responses = ["It is certain",
             "You may rely on it",
             "As I see it, Yes",
             "Outlook Good",
             "Mose likely",
             "It is decidedly so",
             "Without a doubt",
             "Yes definetly"]

while True:
    ques = input("Please ask the magic 8 ball a question")
    if ques == "":
        sys.exit()
    else:
        print(responses[random.randint(0, 7)])
    
