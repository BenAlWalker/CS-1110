temp = input("What is the temperature in Celsius? ")
'''
this is my function :)
'''
temp2 = float(temp)
temp2 = temp2 * 9 * 0.2  # formula from Google: (0°C × 9/5) + 32
temp2 = temp2 + 32
temp2 = round(temp2, 1)
print("It is " + str(temp2) + " degrees Fahrenheit")

