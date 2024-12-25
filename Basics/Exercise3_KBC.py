# Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions
#  and their correct answers. 
# Display the final amount the person is taking home after playing the game.

#  Questions are:

questios = [
    {"Question":"Which of the following countries is the world's largest producer of saffron?",
    "Options" : " A. India  B. USA  C.  Iran   D. Japan"
     },
    {"Question":"Which god is also known as ‘Gauri Nandan’?",
    "Options" : " A. Agni  B. Vayu  C.  Hanuman   D. Ganesha"
     },
    {"Question":"What does not grow on tree according to a popular Hindi saying?",
    "Options" : " A. Money  B. Flower  C.  Tree   D. Fruit"
     },
    {"Question":"Which city is known as the Pink City of India?",
    "Options" : " A. Jaipur  B. Patna  C.  Kolkata   D. Delhi"
     },
    {"Question":"Who wrote India's National Anthem?",
    "Options" : " A. Rabindranath Tagore  B. MK Gandhi  C.  Santosh   D. Bilok"
     },
    {"Question": "How many major religions are there in India?",
    "Options" : " A. 6  B. 7  C.  8   D. 9"
     },
    {"Question":"When is the National Hindi Diwas celebrated?",
    "Options" : " A. 14 September  B. 11 September  C.  12 September   D. 10 September"
     },
    {"Question":"Which country is the largest producer of coffee in the world?",
    "Options" : " A. India  B. USA  C.  Iran   D. Brazil"
     },
    {"Question":"Where is India Gate located?",
    "Options" : " A. Agra  B. Mumbai  C.  New Delhi   D. Patna"
     }
    ]

option =["C","D","A","A","A","A","A","D","C"]
# d =questios[0]
# print(d["Question"])
# print(d["Options"])

prizeMoney =0
i =0

print("Welcome to Santos's KBC Let's Start Playing")
while(i<len(questios)):
    d = questios[i]
    print("Question: ",d["Question"])
    print("Options: ",d["Options"])
    op = input("Type your Option: ")
    if(op== option[i]):
        prizeMoney= prizeMoney+50000;
        print("Congratulations Corrent Answer Your Prize is ", prizeMoney)
    else:
        print("Sorry Worng Answer Your Prize Money is: ", prizeMoney)
        print("Thanks For Playing")
        break
    i=i+1




print("Thanks For Playing Santosh KBC Your Total prize money is ")
print(prizeMoney)