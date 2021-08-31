import random
import time

def ItemRandomizer(items): # Create Random
    randomizedItemSet =  []
    for i in range(3): # Make 3 Random Item sets.
        random.shuffle(items)   
        randomized_items = items.copy() # Make a Copy of Randomized Items.
        randomizedItemSet.append(randomized_items)
    return randomizedItemSet

def Game(items, strikeItems): # Initializes the Game.
    gameIsRunning = True
    numberOfRollsLeft = 10

    while(gameIsRunning == True): # Loop until player wins/looses.
        print('\nYou have', numberOfRollsLeft,'rolls left')

        randomizedItemSet = ItemRandomizer(items)
        input('press \"Enter\" to roll.\n')
        initialItem = None
        matchedItem = None
        for i in range(len(items)): # Create's the column of the table.
            initialItem = None # Reset's initial item
            matchedItem = None # Reset's matched item
            for j in range(3): # Create's the row of the table.
                currentItem = randomizedItemSet[j][i] 
                print('| ', currentItem, ' |', end='')

                if (initialItem == None): # Checks if we dont have initial item yet.
                    initialItem = currentItem # Assign our current item as initial item.
                else:
                    if (currentItem == initialItem and matchedItem == None): # Checks if current item is same as initial item, and checks if we dont have matched items yet. 
                        matchedItem = currentItem # Assigns our current item as matched item.
                    else:
                        if (currentItem == matchedItem): # Checks if current item is same as matched item, assuming that matched item is also ssme with initial item.
                            print(' ~~ Strike! ~~', end='')
                            strikeItems.append(currentItem) # We then add this item to our Striked items.
                            gameIsRunning = False # Set the Game is running into false.
            time.sleep(0.3) # Add pause on every row itteration.
            print()
        numberOfRollsLeft -= 1 # Reduce number of rolls by one
        if (numberOfRollsLeft == 0): # Checks if number of rolls went to zero
            print('\nYou Loose')
            gameIsRunning = False # Ends the Game

def main():
    print('🍒Welcome to Lucky 7🍒')
    strikeItems = []
    items = [' 7', '🍒', '🌸', '🍉', '💩']
    winningMessage = {' 7' : '777 JACKPOT 777', '🍒' : '🍒 CHERRY ON TOP 🍒', '🌸' : '🌸 BLOOM LIKE A FLOWER 🌸', '🍉' : '🍉 YUM YUM 🍉', '💩' : '💩 STEP OUT 💩'}
    comboMessage = ['DOUBLE KILL', 'OH BABY A TRIPLE',  'UR LUCKY FOUR SURE', 'MEGA JACKPOT']
    Game(items, strikeItems)
    print()
    for i in strikeItems:
        for j in items:
            if (j == i):
                print(winningMessage[j])
    for k in range(len(strikeItems)):
        if (k + 2 == len(strikeItems)):
            print('\n'+ comboMessage[k])
main()

