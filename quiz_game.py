print('Welcome To The Quiz Game'.center(50,'-'))
play=True if input("Do you wish to play the game? \n1. Yes \n2. No \nSelect Option (1 or 2 only):")=='1' else False
if play:
    {1:'Aldrin',2:'Gagarin',3:'Armstrong',4:'Collins'}
    questions={'1. Who was the first person to walk on the moon?':
               {1:'Buzz Aldrin',2:'Yuri Gagarin',3:'Neil Armstrong',4:'Michael Collins'},
               '2. What is the capital of Japan?':
               {1:'Seoul',2:'Tokyo',3:'Beijing',4:'Bangkok'},
               '3. Which planet is known as the Red Planet?':
               {1:'Venus',2:'Mars',3:'Saturn',4:'Jupiter'},
               '4. Who wrote the play "Romeo and Juliet"?':
               {1:'William Shakespeare',2:'Charles Dickens',3:' Mark Twain',4:'Jane Austen'},
                '5. What is the chemical symbol for gold?':
               {1:'Au',2:'Ag',3:'Fe',4:'Pb'},
               '6. What is the largest mammal in the world?':
               {1:'African Elephant',2:'Blue Whale',3:'Great White Shark',4:'Polar Bear'},
               '7. In which year did World War II end?':
               {1:'1940',2:'1943',3:'1945',4:'1950'},
               '8. Which country is famous for the Eiffel Tower?':
               {1:'Italy',2:'Spain',3:'France',4:'Germany'},
               '9. What is the hardest natural substance on Earth?':
               {1:'Steel',2:'Diamond',3:'Gold',4:'Quartz'},
               '10. What is the main ingredient in guacamole?':
               {1:'Tomato',2:'Avocado',3:'Cucumber',4:'Potato'}
               }
    answers=iter((3,2,2,1,1,2,3,3,2,2))
    print('About Quiz:')
    print(" -->Thre are 10 Question carry 1 point each")
    print(' -->select an option (i.e, 1,2,3,4) out of corresponding options from the question' )
    print(" -->Not Negitive marking are there")
    print(" -->Final Score is displayed only after successfully complting all scores")
    score=0
    for i,j in questions.items():
        print()
        print(i)
        print(' ','    '.join(map(lambda x:') '.join(map(str,x)),j.items())))
        opt=input("Enter Option:")
        while int(opt) not in (1,2,3,4):
            print("Enter Valid Option to go next Question:")
            opt=input("Enter Option:")
        ans=next(answers)
        if opt==str(ans):
                 print("Correct Answer")
                 score+=1
        else:
                print(f'Incorrect Answer (ANSWER: {ans})')
    if score>9:
        print(f'Excellent!!! You Got {score} Score')
    elif score>7:
        print(f'Good....  , You Got {score} Score')
    elif score>5:
        print(f'Average , You Got {score} Score')
    else:
        print(f'Poor , You Got {score} Score')
else:
    print("OK! Bye...")
    
