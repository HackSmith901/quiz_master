# A random quiz generator program.
import random 

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Create 35 different quizzes.
for quiznum in range(35):
    quiz_file=open("Quiz%s.txt" %(quiznum+1),'w')
    answer_file=open("Answer%s.txt"%(quiznum+1),'w')

    # Write the header to the file 
    quiz_file.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quiz_file.write((" "* 20) + (f"US Capitol's quiz Form{quiznum+1}"))
    quiz_file.write("\n\n")


    # Shuffle the states
    states=list(capitals.keys())
    random.shuffle(states)

    for questnum in range(50):
        correct_answer=capitals[states[questnum]] 
        wrong_answers=list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)] # Deleted the write answer.
        wrong_answers=random.sample(wrong_answers,3)
        options=wrong_answers+[correct_answer]
        random.shuffle(options)

        # Write the questions and answers to the quiz file
        quiz_file.write(f"{questnum+1} What's the capital of {states[questnum]} ?\n")
        for i in range(4):
            quiz_file.write(f"{'ABCD'[i]}. {options[i]}\n")

        quiz_file.write('\n')


        answer_file.write(f"Question{questnum+1} Answer:{'ABCD'[options.index(correct_answer)]}\n")

    quiz_file.close()
    answer_file.close()