def lookup_classes():
    set_classes = set()  #only unique values
    with open("files_11/classlist.csv") as file:
        line = file.readline()
        while line:
            record = line.rstrip().split(';')
            set_classes.add(record[3])
            line = file.readline()
    return set_classes


def control(myclass):
    attendance_list = []  #list
    with open("files_11/classlist.csv") as file:
        line = file.readline()
        while line:
            record = line.rstrip().split(';')
            if record[3] == myclass:
                presence = input(record[2]+' '+record[1]+': ')

                student = record[1]+';'+record[2]+";"
                if presence == '':
                    student += 'OK\n'
                elif presence in 'nN':
                    student += 'NOT\n'
                else:
                    student += '?\n'
                attendance_list.append(student)
            line = file.readline()
    return attendance_list


# main
classes = list(lookup_classes()) #convert to list to sort
classes.sort()
print(*classes)
# for c in classes:
#     print(c)
myclass = input('In which class do you want to do the check: ')
attendance_list = control(myclass)
if len(attendance_list) == 0:
    print("This class doesn't exit")
else:
    with open(myclass+".csv", "w") as output:
        output.write('Attendance list ' + myclass + '\n' )
        output.writelines(attendance_list)
