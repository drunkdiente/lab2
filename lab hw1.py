def roots(a,b,c):
    discr = b**2 - 4*a*c
    if discr < 0:
        return "Корней нет"
    if discr == 0:
        return (-b)/2*a
    if discr > 0:
        x1 = (-b-discr**0.5)/2*a
        x2 = (-b+discr**0.5)/2*a
        return x1,x2
print(roots(1,3,-4))

