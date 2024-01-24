#adding title 
print('\nDISPLAYING DOWNWARD HALF PYRAMID\n')

#this is where you can write the number of asterisk
digital = int(input('ENTER THE NUMBER : '))

#function to rearrange the downward pyramid asterisk
for triangle in range(digital, 0, -1):
    for r in range(1, triangle+1):
        print('* ', end='')
    #this is where it display the downward asterisk    
    print()