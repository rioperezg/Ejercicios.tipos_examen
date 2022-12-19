def Hollow_triangle(n):
    for i in range(1, n+1):
        print(" "*(n-i) + "#" + i*" " + "#" + " "*(n-i))
    return None
print(Hollow_triangle(6))