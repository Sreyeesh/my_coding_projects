"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, ca late her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""

# your code starts here:


quiz_file = open('The_Complete_Python_Course/files_practice/questions.txt', 'r')
questions = quiz_file.readlines()

# print(questions)

quiz_file.close()
correct_answers = 0

number_of_questions = len(questions)
results = open('The_Complete_Python_Course/files_practice/results.txt', 'w')

for line in questions:
    # print(questions)

    question = line.split('=')[0]
    
    answer = line.split('=')[1].strip('\n')

    user_input = input(question + '=')
    
    if user_input == answer:
        correct_answers = correct_answers+1
    # results.write('question was ' + question + '\n')
    # results.write('user answer ' + user_input + '\n')
    # results.write('answer was' + answer + '\n')

    # if user_input == answer:
    #     print("That's right !")
    #     correct_answers = correct_answers+1
    # else:
    #     print("That's wrong!")

# final_score = str(round((correct_answers/number_of_questions)*100))
# print('This is the final score ', final_score)

results.write('Your final score is {}/{}.'.format(correct_answers,number_of_questions))
results.close()
    
    
# results.close()
    
    