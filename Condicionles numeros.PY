x = int(input("Introduce un número 1: "))
y = int(input("Introduce un número 2: "))
z = int(input("Introduce un número 3: "))

Cond1 = (x**2) != (y - z)
Cond2 = (20 <= y <=40)
Cond3 = (-30 <= z <= -15)
Cond4 = ( y * z ) % 2 == 0

print(Cond1 and Cond2 and Cond3 and Cond4) 

if (Cond1 and Cond2 and Cond3 and Cond4):
    print("True")
else: 
    print("False")



