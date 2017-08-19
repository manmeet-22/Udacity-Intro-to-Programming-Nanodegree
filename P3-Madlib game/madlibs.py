#This is Project 3 - MadLibs Game
#This game contains 4 levels.Each level contains 4 questions.
#levels list is used to decide the difficulty level of the questions
levels=[1,2,3,4]

#questions list contains the questions for each level.
questions=["The name of this course is Intro To _1_ Nanodegree.\nThere are _2_ number of projects in this nanodegree.\nThis part of the Nanodegree focus on _3_ Language.\nThe name of this game is _4_ game",
           "Full form of HTML is _1_.\nThis language is used to create _2_ pages.\n_3_ tag is used for largest heading.\n_4_ tag is used to highlight the text.",
           "ROM stands for _1_.\nRAM stands for _2_.\nCD stands for _3_.\n IP stands for _4_.",
           "'Equal to' is an _1_ operator.\nVariables are of _2_ types.\nFunctions are known as set of _3_.\nMachine language is _4_ language."]
#answers list contains the answers foreach question of each level.
answers=[["programming","4","python","madlibs"],
         ['hyper text markup language', 'web', 'h1', 'mark'],
         ['read only memory', 'random access memory', 'compact disk', 'internet protocol'],
         ['assignment', '2', 'instructions', 'binary language']]

#Intro Line
print("\t"*10+"Welcome to MadLibs Game!!\n")
print("\t"*7+"1. Novice\t2. Normal\t3. Intermediate\t4. Expert\n")

# This function is made to replace the empty blanks with the correct answers
def replace(index,element,string):
    """
        Input: 'index' carries the level index entered by the user, So that asnwers are taken from the matching index.
                'element' carries the the index of the current blank position.
                'string' carries the the question string for the user input level.
        Output: returns the replaced correct string
        Behavior: This funtion replaces the blanks and index  by the correct answer.
    """
    string=string.replace("_"+str(element+1)+"_",answers[index][element])
    #replace function is an inbuilt function used to replace some text with another.
    return string

def madlib_game_code(index,current_level_ques):
    """
        Input: 'index' carries the level index entered by the user.
                'current_level_ques' the index of the questions for that particular level in the questions list.
        Output: None
        Behavior:This funtion is where all the process for the game takes place.
                This displays the questions for the particular index of level. If the answer entered is correct,
                    it calls the replace function so that empty blank is replaced with the corect answer..
                If the answer is correct it goes to next blank else reprompts the user for answer.
                Once the last blank answer is filled it shows the number of incorrect attempts by the user.
    """
    print(current_level_ques)
    """current_queston is used as a loop control variable and total_questions is used to store 1+the number of questions for the level. 
    Incorrect_times contains the total of incorrect answer by the user.
    """
    question_index = 1
    total_questions = 5
    incorrect_times =0
    while question_index<total_questions:
        # blank variable stores the input of the user for the current question.
        blank =input("Enter blank "+str(question_index)+" answer - ").lower()
        if blank==answers[index][question_index-1]:
            print("Correct Answer!!")
            current_level_ques = replace(index,question_index-1,current_level_ques)
            print(current_level_ques)
            #Question Index is incresed by one to go to next question
            question_index +=1
        else:
            #As answer is incorrect incorrect_times is incresed by one
            print("Incorrect Answer!!")
            incorrect_times += 1
    print("Your answered ", incorrect_times ," times incorrectly in this Level")

def check_level(level):
    """
        Input: 'level' carries the level index entered by the user
        Output: further call the madlib_game_code function
        Behavior: This funtion checks the level index sent by the user against the levels list. The madlib_game_code is called for that index then.
    """
    index=0
    # index is used as a loop control variable.
    while ( index<len(levels) ):
        if levels[index]==level:
            madlib_game_code(index,questions[index])
        index+=1
        
def start_madlibs():
    """
        Input: none
        Output: none
        Behavior: This function is called at the first step of the game. It takes user's level choice and checks if the choice is valid or not and hence start the game.
         When the questions of particular levels are over, it prompts the user whether the he/she wants to continue or quit.
        """
    #This function takes input from user for level and checks whether the entered level exists or not.
    level = int(input("Please choose your level : "))
    #level variable stores the value of level entered by the user. 
    if(level==levels[0] or level==levels[1] or level==levels[2] or level==levels[3]):
        check_level(level)
    else:
        print("Enter valid Level")
        start_madlibs()  
    user_input=input("Do you want to play again?? \nEnter 'Yes' to Play again or 'Quit' to exit").lower()
    if user_input=="yes":
        print("\n")
        start_madlibs()
    else:
        print("Thank You, Have a Nice Day")

start_madlibs()
