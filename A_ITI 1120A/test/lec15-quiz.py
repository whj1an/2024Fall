import random

#0: question
#1-4: 4 possible answers
#5: Category
#6: difficulty

def ask_question(q, p):
        print()
        print(q[0])
        for i in range(1, 5):
                print(i,   q[ p[i-1] ])
        
def raw_read_answer():
        try:
                ans = int(input("Answer (1, 2, 3 or 4): "))
                return ans
        except ValueError:
                print("Error. Answer must be an integer.")


def read_answer():
        ans=raw_read_answer()
        while ans not in [1,2,3,4]:
                print("Answer must be 1, 2, 3 or 4")
                ans=raw_read_answer()
        return ans         

# main        
lines=open('quiz.csv').read().splitlines()
questions=[]
for line in lines:
        questions.append(line.split('\t'))

lives = 5
score = 0 

while lives >= 1:

        p=[1,2,3,4]
        random.shuffle(p)
        q=random.choice(questions)
        print("difficulty", q[-1], q[-2], q[-3])
        ask_question(q, p)
        ans=read_answer()
    


        if p[ans - 1] == 1:
                print("Correct")
                score = score + int(q[-1])       
        else:
                print("Incorrect. The correct answer is:", q[1])
                lives = lives  - 1
        print("You have", lives, "lives left. Your score is: ", score)  
                



                
