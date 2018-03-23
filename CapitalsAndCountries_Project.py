__author__ = 'Adeel'
#Step 1: Open file, get input from user
#Step 2: Create function that takes input from user and perform search operation like if user enter country then its capital would be printed, if user enter capital its country would be printed
#Step 3: If user enter any currency then its country would be printed. e.g. if you enter Euro all countries would be printed in which euro is currecny

#capitals.csv file need to be in the same directory as the program. Name of country should be entered as it is entered in the file.

import csv

def  GetData(var,data):
    discover=0
    with open('capitals.csv','r') as data:
        for row in data:
            row = row.strip().split(',')
            if(var=="region"):
                if row[0]==region:
                    print 'The capital of ',row[0],'is',row[1]
                    print "-" * 20
                    discover=1
                    break
                else:
                    if row[1]==region:
                        print 'The country of ',row[1],'is',row[1]
                        print "-" * 20
                        discover=1
                        break
            else:
                if(var=="currency"):
                    if row[2]== currency:
                       print row[0]
                       discover=1




        if discover == 0:
            print("Nothing found against the Input you provided, remember to use capital letters!")

while True:
    region=raw_input('What country do you want to look for? ')
    GetData("region",region)
    currency=raw_input("what currency do you want to look for ").lower()
    GetData("currency",currency)
    print 'Do you want any other info? y/n '
    user_choice=raw_input().lower()
    if user_choice=='y':
        continue
    else:
        break
