def read_books():
    books = []
    with open("books.txt") as file:
        line = file.readline().rstrip()
        while line:
            books.append(line)
            line = file.readline().rstrip()
    return books


def menu():
    # choice = '?'
    print('\ta - Overview\n\tb - Longest title\n\tc - 5 letters on a row\n\ts - Stop ')
    choice = input('\tMake your choice: ').lower()
    while choice not in 'abcs':
        print('\ta - Overview\n\tb - Longest title\n\tc - 5 letters on a row\n\ts - Stop ')
        choice = input('\tMake your choice: ').lower()
    return choice


def print_list(books):
    print('\nList of books:\n')
    for i in range(len(books)):
        print(i+1, books[i])
    print()


# hoofdprogramma
list_books = read_books()
choice = menu()


while choice != 's':
    if choice == 'a':
        print_list(list_books)
    elif choice == 'b':
        #print_list(list_books)
        max_length = len(list_books[0])
        for i in range(len(list_books)):
            if len(list_books[i]) > max_length:
                max_length = len(list_books[i])
        print('The longest title has', max_length, 'characters\n')
    elif choice == 'c':
        booknumber = int(input("Enter booknumber max " + str(len(list_books)) +": "))
        book = list_books[booknumber-1]

        for i in range(len(book)):
            if i % 5 == 0:
                print()
            print(book[i], end=' ')
        print()
    choice = menu()
