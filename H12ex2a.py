def control(myclass):  #var die opgevuld wordt in hoofdprogramma
    attendance_list = []  #list

    with open("classlist.csv", encoding='utf-8') as file:
        line = file.readline()
        while line:
            # r0846652;ABID;ADAM;1 ACS 02
            record = line.rstrip().split(';')
            if record[3] == myclass:
                presence = input(record[2]+' '+record[1]+': ')
                student = record[1]+';'+record[2]+";"
                if presence == '':
                    student += 'OK\n'
                elif presence in 'n'.lower():
                    student += 'NOT\n'
                else:
                    student += '?\n'  #foutieve invoer
                attendance_list.append(student)
            line = file.readline()
    return attendance_list


# main program
input_myclass = input('In which class do you want to do the check: ')
create_attendance_list = control(input_myclass)  #oproepen functie van met return dus vergeet niet om resultaat op te vangen!!!
# print(attendance_list)

if len(create_attendance_list) == 0:
    print("This class doesn't exit")
else:
    with open(input_myclass+".csv", "w") as output:  #write not append
        output.write('Attendance list ' + input_myclass + '\n' )
        output.writelines(create_attendance_list)
