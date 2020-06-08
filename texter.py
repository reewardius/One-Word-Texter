# Import modules
from time import sleep
from os import system

# Define head
def head():
    system('clear')
    system('cat head.txt')
    print("")
    print("")

# Ask for details
#API-URL
head()
print("Please, create a Chat-API account, if you don't have it already.")
print("If you have a Chat-API account, Please enter your API-URL below.")
print("")
url = input("API-URL: ")
#Phone number
head()
print("Please, enter the recievers phone number below.")
print("With the country code and without the +.")
print("")
phone = input("Phone: ")
# Delay
head()
print("What should be the delay between each word?")
print("In seconds.")
print("")
delay = input("Delay: ")
# Script
head()
print("What's the name of the file you want to send?")
print("By default, it's the script to Bee Movie from the BeeMovie.txt file.")
print("")
file = input("File: ")
#If default set deafult
if file == "":
    file = "BeeMovie.txt"
#If not entered, exit
if url == "" or phone == "" or delay == "":
    head()
    input("Please, enter all the details. Press enter to exit.")
    exit(1)
#Check if phone is a number
try:
    float(phone)
except ValueError:
    head()
    input("Please, enter a phone number as a number without the +. Press enter to exit.")
    exit(1)
#Check if delay is a number
try:
    float(delay)
except ValueError:
    head()
    input("Please, enter the delay as a number in seconds. Press enter to exit.")
    exit(1)

# Create a list of words from the text file
#Load the file
file1 = open(file)
#Convert it into a string
file2 = file1.read()
#Remove unneeded bullshit
file3 = file2.replace('\n', '')
#Split it into words and convert it into a list
wordlist = file3.split()

head()
sleep(int(delay))

# Start sending the script
for i in range(len(wordlist)):
    #Set data
    data = 'phone=' + phone + '&body=' + wordlist[i]
    #Display data
    print(data)
    #Send request
    system('curl --data "' + data + '" ' + url)
    print("")
    #Wait some time
    sleep(int(delay))

# Display done and exit
head()
input("Done! Press enter to exit.")
exit(1)
