# Parseme.py

test_line = "cutty;https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg;gray/white;3"
# We want to split test_line like this:
# ["cutty","https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg", "gray/white", "3"]

def parse_line(line): 
    #TODO

    print ("Nom:", line[0])
    print ("Color:", line[2])
    print ("Age: ", line[3])

parse_line(test_line)



""" TODO

fhand = open('cats.txt')
list = split("\n", fhand)

def parse_file(): 
    for i in len(list):
       print ("Nom:", list[i,0])
parse_file()

"""


###############################################

# i = 0

# def incr(i):
#     i += 1
#     print(i)    # 1
#     return i

# print(i)        # 0
# j = incr(i)
# print(j)        # 1
# print(i)        # 0