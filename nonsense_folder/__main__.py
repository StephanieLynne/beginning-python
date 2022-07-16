size = 5
design = "a"
t_formula = size * 2 + 1
for _ in range(size):
    print( design * size )
for i in range(1, (t_formula), 2):
    tri = ( design * i )
    tri_cent = tri.center(size * 2)
    print(tri_cent)
for i in range((size +2), 0, -2):
    dia = (design * i)
    dia_cent = dia.center(size * 2)
    print(dia_cent)
last_line = (design * size)
#ll_cent = 