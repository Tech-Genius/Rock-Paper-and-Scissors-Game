import random

possible_outcome = ["R", "P", "S"]
computer_move = random.choice(possible_outcome)


IsValidOption = False
print("******Welcome To The Rock, Paper and Scissors Game**********")
while IsValidOption == False:
    print("Enter P to choose Paper")
    print("Enter R to choose Rock")
    print("Enter S to choose Scissors")
    user_move = input("Enter Your Choice:\n")    
    if(user_move in possible_outcome):
        IsValidOption = True
        
        print("Computer move is", computer_move, "and your move is", user_move)
        if(user_move == computer_move):
            IsValidOption = False
            print("Tie! No Winner! Play Again")
            
            
        elif(user_move == "R" and computer_move == "S"):
            print("Rock Beats Scissors....You Win")
        elif(user_move == "S" and computer_move == "R"):
            print("Rock Beats Scissors....You Loose")  
        elif(user_move == "P" and computer_move == "R"):
            print("Paper Beats Rock....You Win")      
        elif(user_move == "R" and computer_move == "P"):
            print("Paper Beats Rock....You Loose")
        elif(user_move == "S" and computer_move == "P"):
            print("Scissors Beats Paper....You Win")
        elif(user_move == "P" and computer_move == "S"):
            print("Scissors Beats Paper....You Loose")  
    else:
        print("You Selected A Wrong Option! Try Again") 
           
    
                  
        


       

              
   



   
