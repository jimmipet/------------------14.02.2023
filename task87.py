import cmath
z = 4
r = abs(z)
theta = cmath.phase(z)
roots = [cmath.rect(r**(1/3), (theta + 2*k*cmath.pi)/3) for k in range(3)]
for root in roots:
    print(root)
