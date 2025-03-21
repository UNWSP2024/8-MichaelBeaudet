# Title: Program 1 Week 8
# Author: Michael Beaudet
# Date: 3/21/25

def initials_generator(personsName):

    personsInitials = ""
# Split the name
    name_parts = personsName.split()
# Loop through and get each first letter of each name
    for part in name_parts:
        personsInitials += part[0].upper() + ". "

    return personsInitials.strip()
# Get the user's full name
personsName = input('Enter the users first, middle, and last name: ')
# Call the function
initials = initials_generator(personsName)
# Display the results
print(initials)