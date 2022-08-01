# Kayla Terrell
# Intro To Programming
#07/09/2022
#Functions
#This program will convert miles to kilometers
print('Start')
NbrMilesStr = input('How many miles were driven?')


def convert_distance(miles):
    Nbrmiles = float(NbrMilesStr)
    total = float(Nbrmiles * .621371)


print(f'The total miles driven equals {total} kilometers')
print('End')
