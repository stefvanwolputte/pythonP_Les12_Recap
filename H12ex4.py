def lowest_price():
    prices = {}  #dictionary
    with open('prices.txt') as file:
        line = file.readline().rstrip()
        record = line.split(';')  # je moet hier 2x splitten
        while line:
            item_ind = record[0]  #grouping by item
            lowest_price = record[1]
            while line and record[0] == item_ind:
                if float(record[1]) < float(lowest_price):
                    lowest_price = record[1]
                line = file.readline().rstrip()
                record = line.split(';')
            prices[item_ind] = lowest_price  #create key/value pair -> value = key as index
    return prices


#MAIN FUNCTION
print(lowest_price()) #test van functie

prices_dict=lowest_price()  #oproep van de functie
print('Price list')
print(len('price list')*'-')

for item in prices_dict:
    print(item, '\t', prices_dict[item])   #print key and the value -> value opvragen via naam van dict and key as index
print()

item=input('Enter the item (press x if you want to stop):')#step 1
while item.upper() !='X': #step 2
    if item not in prices_dict:  #step 3
        print('This item is not available')
    else:
        print('The lowest price of ', item.lower(),'is', prices_dict[item], 'EUR')  #item -> key prices[item]-> value
    item = input('Enter the item (press x if you want to stop):')  # step 4
