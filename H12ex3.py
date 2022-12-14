import json
from random import randint


def read_figures():
    with open('figures.json') as jsonfile:
        figures=json.load(jsonfile)
    return figures


def read_names():
    names=[]
    with open('names.txt') as txtfile:
        line=txtfile.readline().rstrip()
        while line:
            record=line.split('/')
            random_number=randint(0,4)
            random_name=record[random_number]
            names.append(random_name)
            line=txtfile.readline().rstrip()
        names.sort()
        # print('length:',len(names))
        # print(*names)
        return names



figuresdef=read_figures()
# print(figuresdef)
new_figures=figuresdef['figures']
# print(new_figures)

nameslist=read_names()
# print(nameslist)

print(f'A figure has been chosen for the following toddlers:')
for name in nameslist:
    length=len(name)
    figure=new_figures[length-1]
    print(f' For {name} a {figure["shape"]} with a {figure["colour"]} colour')
