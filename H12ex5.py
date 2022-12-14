import json
import matplotlib.pyplot as plt

def plotBar(X,Y):
    plt.bar(X, Y)
    plt.title(namecourse)
    plt.ylabel('Average Results')
    plt.xlabel("Years")
    plt.yticks(range(0, 21, 2))
    plt.show()


#Get dict from JSON
with open("results.json") as json_file:
    resultsdict = json.load(json_file)

#Seperate list from Dict
courseslist = resultsdict["courses"]
print(courseslist, type(courseslist))

print('These courses are available\n')

#Seperate classes in Dict with index number
coursedict = {}
counter = 1
for course in courseslist:
    # print(str(counter) + ': ' + course["name"])
    print(str(counter)+ ":",course["name"])
    coursedict[str(counter)] = course["name"]  #create key-value pairs (key:1,...)  key of type string
    counter+=1
print()

#Ask user input
choice = input('Please enter the number of a course: ')
namecourse = coursedict[choice]  #via key 1 or 2
#print(coursedict)
print()
print('The selected course is ' + namecourse)

#look-up data from classes to calculate average
listXaxes = []
listYaxes= []

for course in courseslist:                          #Loop over all courses
    if course["name"] == namecourse:                #check if course matches user input
        academicyears = course["academicyears"]     #get list of all academic years
        for year in academicyears:                  #loop over all years in list
            listXaxes.append(year["ayear"])         #Get the year for the X axis
            scores = year["scores"]                 #get list with all scores
            total =number = 0                       #reset nr studentens +scores
            for score in scores:                    #loop over all scores in that year
                total += int(score["result"])       #add up all scores
                number += 1                         #add sutdent counter with 1
            listYaxes.append(total/number)          #average

print("listXaxes=", listXaxes)
print("listYaxes=",listYaxes)

#Print bar plot
plotBar(listXaxes,listYaxes)


