# Ben Walker (baw3hg) and Kieran O'Dell (kfo7qb)

import math
import webbrowser

# DO NOT MODIFY the following function; use as is
def distance_between(lat_1, lon_1, lat_2, lon_2):
    '''Uses the "great circle distance" formula and the circumference of the earth
    to convert two GPS coordinates to the miles separating them'''
    lat_1, lon_1 = math.radians(lat_1), math.radians(lon_1)
    lat_2, lon_2 = math.radians(lat_2), math.radians(lon_2)
    theta = lon_1 - lon_2
    dist = math.sin(lat_1)*math.sin(lat_2) + math.cos(lat_1)*math.cos(lat_2)*math.cos(theta)
    dist = math.acos(dist)
    dist = math.degrees(dist)
    dist = dist * 69.06         # 69.09 = circumference of earth in miles / 360 degrees
    return dist

from urllib.request import urlopen

closest = 100000

address = ''
addresspart2 = ''
addresspart3 = ''

u = urlopen("http://cs1110.cs.virginia.edu/files/wendys.csv")

lat_1 = float(input("Input a Latitude: "))

lon_1 = float(input("Input a Longitude: "))

for line in u:
    line = str(line)
    line = line.strip('b"')
    line = line.strip("'")
    line = line.strip("\\n")
    line = line.split(",")

    lat_2 = line[0]
    lon_2 = line[1]



    closest1 = distance_between(float(lat_1), float(lon_1), float(lat_2), float(lon_2))
    if closest > closest1:
        closest = closest1
        address = line[4]
        addresspart2 = line[5]
        addresspart3 = line[6]

megaddress = str(address + addresspart2 + addresspart3)
megaddress = megaddress.replace(' ', '+')

webbrowser.open('http://maps.google.com/maps?q=' + megaddress)
