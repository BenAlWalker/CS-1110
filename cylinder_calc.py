#Kieran(kfo7qb) and Ben(baw3hg)

r = float(input("What's the radius of your cylinder? "))
h = float(input("What's the height of your cylinder? "))
pi = float(3.14)

def surface_area(r, h):
    sa = float(2 * pi * r * h + 2 * pi * r * r)
    sa = round(sa, 2)
    return sa
sa = surface_area(r, h)

def lateral_area(r, h):
    la = float(2 * pi * r * h)
    la = round(la, 2)
    return la
la = lateral_area(r, h)

def base_area(r):
    ba = float(pi * r * r)
    ba = round(ba, 2)
    return ba
ba = base_area(r)

def print_cylinder(r, h, sa, la, ba):
    print("Radius:", r)
    print("Height:", h)
    print("Surface Area:", sa)
    print("Lateral Area:", la)
    print("Base Area:", ba)

print_cylinder(r, h, sa, la, ba)