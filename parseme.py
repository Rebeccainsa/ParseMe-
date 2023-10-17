# Parseme.py
#from PIL import Image

# creating a object
#im = Image.open("https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpeg")

#im.show()

import re #contient la fonction split pour la fonction parse_line 

x=["cutty","https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg", "gray/white", "3"]

def parse_line(): 
    print ("Nom:", x[0])
    print ("Color:", x[2])
    print ("Age: ", x[3])

parse_line()


fhand = open('cats.txt')
list=re.split("\n", fhand)

#def parse_file(): 
    #for i in len(list):
       # print ("Nom:", list[i,0])
#parse_file()
