#----------------
#FP2-S01-External Files
#Hailey-lynn Aldred
#29 March 2025
#----------------

#What are the benefits of external files? External files allow for information to be saved, stored, and accessed
#at a later date. External files can be strings or numbers, and can contain large amounts of text within them.
#I used this to my advantage and used a file for the intro of the project, so that my code wasn't so crowded.
#External files can be used for game saves or character saves, as they can have information put into them, which
#they will hold until it is reopened. This can include things like character level, health, experience, or inventory.
#These aspects can be preset, or input by the user (as seen in my project). External files can also be used for
#accessing specific pieces of data, because external files can be turned into lists.

#----Functions----#
def start():
    #reading the prologue .txt file
    intro = open('Creator Intro.txt', 'r') #imports the file and opens it for reading
    create = intro.read()#saves the opened file to the variable create
    print(create)#prints the variable which is the .txt file
    intro.close()#closes the file so that it doesn't corrupt
    
def char_creation():
    char_name = input("What is your character's name? > ")#user input
    coin_number = input("What is your favourite number? > ")
    eyes = input("What colour are your character's eyes? > ")
    hair = input("What colour is your character's hair? > ")
    shirt = input("What is your favourite colour? > ")
    pants = input("What is your second favourite colour? > ")
    shoes = input("What is your third favourite colour? > ")
    
#takes user input and turns it into a file name
    char_file = char_name + '.txt'
    avatar = open(char_file, 'w')#opens that new file and allows for writing to be added
    avatar.write('Name: ')
    avatar.write(char_name + '\n') #takes the user input and writes it into the file
    avatar.write('Coins: ')
    avatar.write(coin_number + '\n')
    avatar.write('Eye Colour: ')
    avatar.write(eyes + '\n')
    avatar.write('Hair Colour: ')
    avatar.write(hair + '\n')
    avatar.write('Shirt Colour: ')
    avatar.write(shirt + '\n')
    avatar.write('Pants Colour: ')
    avatar.write(pants + '\n')
    avatar.write('Shoe Colour: ')
    avatar.write(shoes)
    avatar.close()#closes the file to avoid corruption
 
#opens the file we made with the user input for reading
    avatar_view = open(char_file, 'r') 
    print("Here is your character information!")
    details = avatar_view.read()#reads the file
    print(details)#prints the file we just read
    print("Because your favourite number is", coin_number, "we've given you", coin_number, "coins!")
    print("Isn't that awesome?")
    avatar_view.close()
    
def main():
    loop = True #project loop
    while loop == True:
        start() #calls the start function
        char_creation()
        print("You're character is super cool! Would you like to make another one? 'y' or 'n'?")
        again = input('> ').lower()#turns the user input into lowercase
        if again == 'y':
            loop = True #if again = y, the project reruns
        elif again != 'y': #if again doesn't = y, the project stops running
            print("Thank you for playing!")
            loop = False
#----Main Code----#
#muffled screaming#
main()#calls function main

#not everything has comments because there's some repetitive stuff
