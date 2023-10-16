# Parseme.py
#from PIL import Image

# creating a object
#im = Image.open("https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpeg")

#im.show()

x=["cutty","https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg", "gray/white", "3"]

def parse_line(): 
    print ("Nom:", x[0])
    print ("Color:", x[2])
    print ("Age: ", x[3])

parse_line()


def parse_file(): 
    fhand = open('cats.txt')
    parse_line(fhand)
    