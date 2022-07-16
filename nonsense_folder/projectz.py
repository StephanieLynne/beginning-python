title = "LET'S MAKE SHAPES WITH REPEATING CHARACTERS!"
cent = title.center(100)
print(cent)
size = 8
design = "!"
def square_make():
    for i in range(size):
        print(design * size)
square_make()

shape = input("Choose square, triangle, or diamond: ")
size = ("Type integer to choose size: ")
design = ("Choose any single character from keyboard")
print(shape)