import sys

with open("data.csv", "w") as file:

    file.write("Name, age, nationality, gender, education\n")
    file.write("sam, 25, usa, male, highschool\n")
    file.write('alan, 65, norway, male, masters\n')
    file.write('samira, 23, kenyan, female, highscool\n')
    file.write('zara, 55, swedish, female, phd\n')
    file.write('sofia, 35, finland, female, bachelor') 

print ("CSV file has been creates successfullt as: 'data.csv'.")

with open("data.csv", "a") as file:
    file.write(",".join(sys.argv[1:]) + "\n")
print("row added successfullty.")

#result

# Name, age, nationality, gender, education
# sam, 25, usa, male, highschool
# alan, 65, norway, male, masters
# samira, 23, kenyan, female, highscool
# zara, 55, swedish, female, phd
# sofia, 35, finland, female, bachelor