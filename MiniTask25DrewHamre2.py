#
# Author: Drew Hamre
# Date: 4/17/23
# Description: 
#

# Constants used to refer to the parts of the quiz question
CATAGORY = 0
VALUE = 1
QUESTION = 2
ANSWER = 3

#
# Splits a String containing all question information, then
# returns the specified part of the question
#
#
# Parameters
#   question - String containing comma separated quiz question details
#   whichInfo - constant representing which part of the question to return
#                should be one of CATEGORY, VALUE, QUESTION, ANSWER
# Return
#   String containing the specified part of the question
def getInfo(question, whichInfo):
    newList = question.split(",")
    print(newList[whichInfo])
    
    return ""

####################################
## Data
###################################

#
# Single string containing CSV formatted quiz question
#  "category,pointvalue,question,answer"
#
singleQuestionCSV = "Cats,100,Cats hate this,water"

#
# List of strings containing CSV formatted quiz data
#
questionList = ["Dinos,500,My existence has been debated but I have very long neck,brontosaurus",
                "Cats,200,This killed the cat,curiosity",
                "Math,200,Square me to get 100,10",
                "Dinos,100,Famous carnivore,t-rex",
                "Cats,400,Tiger + Lion =,liger",
                "Dinos,400,Turns out dinosaurs were covered in these,feathers",
                "Math,200,You wish you could eat this numerical constant,pi",
                "Math,400,It measures round and round and round,circumference",
                "Math,100,2 + 2 =,4",
                "Dinos,200,They have three horns,triceratops"]

print(" ")
QuestionsInList0 = (questionList[0])
print(QuestionsInList0)
QuestionsInList1 = (questionList[1])
print(QuestionsInList1)
QuestionsInList2 = (questionList[2])
print(QuestionsInList2)
QuestionsInList3 = (questionList[3])
print(QuestionsInList3)
QuestionsInList4 = (questionList[4])
print(QuestionsInList4)
QuestionsInList5 = (questionList[5])
print(QuestionsInList5)
QuestionsInList6 = (questionList[6])
print(QuestionsInList6)
QuestionsInList7 = (questionList[7])
print(QuestionsInList7)
QuestionsInList8 = (questionList[8])
print(QuestionsInList8)
QuestionsInList9 = (questionList[9])
print(QuestionsInList9)

print(" ")
SplittingQuestions0 = QuestionsInList0.split(",")
print(SplittingQuestions0)
SplittingQuestions1 = QuestionsInList1.split(",")
print(SplittingQuestions1)
SplittingQuestions2 = QuestionsInList2.split(",")
print(SplittingQuestions2)
SplittingQuestions3 = QuestionsInList3.split(",")
print(SplittingQuestions3)
SplittingQuestions4 = QuestionsInList4.split(",")
print(SplittingQuestions4)
SplittingQuestions5 = QuestionsInList5.split(",")
print(SplittingQuestions5)
SplittingQuestions6 = QuestionsInList6.split(",")
print(SplittingQuestions6)
SplittingQuestions7 = QuestionsInList7.split(",")
print(SplittingQuestions7)
SplittingQuestions8 = QuestionsInList8.split(",")
print(SplittingQuestions8)
SplittingQuestions9 = QuestionsInList9.split(",")
print(SplittingQuestions9)
print(" ")

questionListCatagory0 = SplittingQuestions0[0]
questionListValue0 = SplittingQuestions0[1]
questionListQuestion0 = SplittingQuestions0[2]
questionListAnswer0 = SplittingQuestions0[3]\

print(" ")
print("CATEGORY: " + (questionListCatagory0))
print("VALUE: " + (questionListValue0))
print("QUESTION: " + (questionListQuestion0))
print("ANSWER: " + (questionListAnswer0))
print(" ")

questionListCatagory1 = SplittingQuestions1[0]
questionListValue1 = SplittingQuestions1[1]
questionListQuestion1 = SplittingQuestions1[2]
questionListAnswer1 = SplittingQuestions1[3]

print(" ")
print("CATEGORY: " + (questionListCatagory1))
print("VALUE: " + (questionListValue1))
print("QUESTION: " + (questionListQuestion1))
print("ANSWER: " + (questionListAnswer1))
print(" ")

questionListCatagory2 = SplittingQuestions2[0]
questionListValue2 = SplittingQuestions2[1]
questionListQuestion2 = SplittingQuestions2[2]
questionListAnswer2 = SplittingQuestions2[3]

print(" ")
print("CATEGORY: " + (questionListCatagory2))
print("VALUE: " + (questionListValue2))
print("QUESTION: " + (questionListQuestion2))
print("ANSWER: " + (questionListAnswer2))
print(" ")

for i in





#####################################
## Main
#####################################

### Step One ###

# Split singleQuestionCSV using a comma as a delimiter and store the result in a new list

singleQuestionCSV = "Cats,100,Cats hate this,Water"
singleQuestionList = singleQuestionCSV.split(",")
#print(singleQuestionList)

# Use the constants at the top of the file to access the pieces of the question.
# Print the information, one part per line.
# Label each part when you print it.

Catagory = singleQuestionList[0]
Value = singleQuestionList[1]
Question = singleQuestionList[2]
Answer = singleQuestionList[3]

#print("CATAGORY: " + (Catagory))
#print("VALUE: " + (Value))
#print("QUESTION: " + (Question))
#print("ANSWER: " + (Answer))


### End Step One ###

### Step Three ###

# Print the information again, but this time 
# call getInfo to get each part

CatagoryFunc = getInfo(singleQuestionCSV, CATAGORY)
#print(CatagoryFunc)
ValueFunc = getInfo(singleQuestionCSV, VALUE)
#print(ValueFunc)
QuestionFunc = getInfo(singleQuestionCSV, QUESTION)
#print(QuestionFunc)
AnswerFunc = getInfo(singleQuestionCSV, ANSWER)
#print(AnswerFunc)

### End Step Three ###

### Step Four ###

# Use len to print how many questions are in the questionList

#numQuestions = len(questionList)
#print("number of questions is:", + numQuestions)

# Use a for loop to print the category and value of each question in questionList

#print("CATEGORY -- VALUE")
#for i in questionList:
    #print("  " + (Catagory) + "  --   " + (Value))
    


### End Step Four ###
