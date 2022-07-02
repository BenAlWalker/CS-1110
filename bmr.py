# Ben Walker, baw3hg


def st_jeor(mass, height, age, sex):
    mass = float(mass * 10)
    height = float(height * 6.25)
    age = float(age * 5.0)
    if sex == "male":
        sex = float(5.0)
    else:
        sex = float(-161.0)
    p = mass + height - age + sex
    return p
