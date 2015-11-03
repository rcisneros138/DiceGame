import random
class DiceGame(object):
    import random
    def __init__(self):
        self.playerOneScore = 0
        self.playerTwoScore = 0
        self.Winner = False
        self.playerOneTurn =True
        print("/////////////////////////////////////////////")
        print("//Guess Your opponants roll number to Win!///")
        print("/////////////////////////////////////////////")

    def ChooseSixSided(self):
        min = 1
        max = 6
        self.sixSidedRoll = (random.randint(min,max))
        dg.PromptUserForRoll(self.sixSidedRoll)
        

        
    def ChooseTwelveSided(self):
        min = 1
        max = 12
        self.twelveSidedRoll=(random.randint(min,max))
        dg.PromptUserForRoll(self.twelveSidedRoll)
        

    def ChooseDiceType(self):
        userChoice = (str(raw_input("Choose Dice Type: 6 sided, or 12 Sided:  ")))
        if userChoice == "6":
            dg.ChooseSixSided()
        elif userChoice == "12":
            dg.ChooseTwelveSided()
        else:
            print("Please Enter a valid Dice Choice: ")
            dg.ChooseDiceType()
        
    
    def PromptUserForRoll(self, actualRoll):
        promptRoll = (str(raw_input("Press 'R' to roll Dice  ")))
        if promptRoll == 'r' and self.playerOneTurn == True:
            dg.PlayerOneRollDice(actualRoll)
        elif promptRoll == 'r' and self.playerOneTurn == False:
            dg.PlayerTwoRollDice(actualRoll)
            
        else:
            print("press r")
            dg.PromptUserForRoll()
       
        
        
    def PlayerOneRollDice(self, actualRoll):
        
        self.PlayerOneRoll = actualRoll
        print("Player One has Rolled")
        print(self.PlayerOneRoll)
        return self.PlayerOneRoll

    def PlayerTwoRollDice(self, actualRoll):
        
        self.PlayerTwoRoll = actualRoll
        print("player Two has Rolled")
        print(self.PlayerTwoRoll)
        return self.PlayerTwoRoll
      

    def BetOnRoll(self):
        if  self.playerOneTurn == True:
            try:
                playerBetAmount =(int(raw_input("Player Two, enter the amount you'd like to bet:  ")))
                PlayerTwoGuess = (int(raw_input("Player Two Guess Player one Dice roll Amount: ")))   
                if PlayerTwoGuess == self.PlayerOneRoll:
                    print("Correct! The Number rolled was: " + (str(self.PlayerOneRoll)))
                    
                    dg.UpdatePlayerOneScore(playerBetAmount)
                    
                else:
                    print("Incorrect!")
                    print("Your Score Remains at: " +(str(self.playerOneScore)))
            except ValueError:
                print("Please Enter a number")
                dg.BetOnRoll()
                      
        else:
            try:
                playerBetAmount =(int(raw_input("Player One, enter the amount you'd like to bet:  ")))
                PlayerOneGuess = (int(raw_input("Player One Guess Player Two Dice roll Amount: ")))
                if PlayerOneGuess == self.PlayerTwoRoll:
                    print("Correct! The Number rolled was: " + (str(self.PlayerTwoRoll)))
                    
                    dg.UpdatePlayerTwoScore(playerBetAmount)

                else:
                    print("Incorrect!")
                    print("Your Score Remains at: " +(str(self.playerTwoScore)))
            except ValueError:
                print("Please Enter a number")
                dg.BetOnRoll()
        

    def UpdatePlayerOneScore(self, betAmount):
        self.playerOneScore += betAmount
        print("Player One Score is now: " + (str(self.playerOneScore)))
        self.playerOneTurn = False
        if self.playerOneScore >= 10:
            self.Winner = True
            
    def UpdatePlayerTwoScore(self, betAmount):
        self.playerTwoScore += betAmount
        print("Player Two Score is now: " + (str(self.playerTwoScore)))
        self.playerOneTurn = True
        if self.playerTwoScore >= 10:
            self.Winner = True
            
       
      
    def MainFunction(self):
        dg.ChooseDiceType()
        dg.BetOnRoll()      
        if self.Winner == False:
            dg.MainFunction()
        else:
            print("Winner!")
            dg.GetWinnerInfo()

    def GetWinnerInfo(self):
        print("Congrats Supreme Champion of ULTIMATE DICE! Let your name be known for EONS!")
        userName = (str(raw_input("Enter your glorious name:  ")))
        scoreTxtFile = open('VictoriousOnes.txt', 'a')
        scoreTxtFile.write("Name: %s" %userName + '\n')


dg = DiceGame()
dg.MainFunction()


