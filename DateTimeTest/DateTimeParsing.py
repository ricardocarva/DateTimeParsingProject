from datetime import datetime

def try_parsing_date(dateSTR):
    #Loops through all possible formats in the list
    for fmt in ("%m/%d/%y %H:%M", "%m/%d/%Y %H:%M", "%m/%d/%y %H:%M:%S"):
        #Try to use the datetime method string parse time. Input is the string to be parsed, and the format from the list above
        try: 
            #If succesful, returns parsed value
            return datetime.strptime(dateSTR, fmt)
        #If it encounters a Value Error, nothing happens but continue to loop
        except ValueError:
           pass
    #If it finds no format that fits the input, we raise an exeption
    raise ValueError('no valid date format found')
 

#Input string to be tested
date_time_str = "09/18/22 @ 15:50:32"

#Strips the string by its blank spaces
date_time_stripped = date_time_str.split(" ")

#Using list comprehension, we will create a list looping through the input string that was stripped to find matches that contains "/" or ":". 
#These should be the values we can actually use to parse the time.
#By doing this we remove any "at" or "@" or invalid characters in the date time entry
listDT = ([item for item in date_time_stripped if "/" in item or ":" in item])

#Then, we join the valid date time fragments we found above.

dateSTR = " ".join([str(item) for item in listDT])

#print them to check
print(dateSTR)

#create a date variable with the value returned by try_parsing_date
date = try_parsing_date(dateSTR)

#Prints value
print(date)
