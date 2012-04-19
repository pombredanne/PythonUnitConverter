def meters_millimeters(n):
    b = float(n) * 1000
    if  float(n) == 1:
        print str(n) + ' meter = ' + str(b) + ' millimeter(s).'
        quit()
    else:
        print str(n) + ' meters = ' + str(b) + ' millimeter(s)'
        quit()

def meters_centimeters(n):
    b = float(n) * 100
    if  float(n) == 1:
        print str(n) + ' meter = ' + str(b) + ' centimeter(s).'
        quit()
    else:
        print str(n) + ' meters = ' + str(b) + ' centimeter(s)'
        quit()

def meters_decimeters(n):
    b = float(n) * 10
    if  float(n) == 1:
        print str(n) + ' meter = ' + str(b) + 'decimeter(s).'
        quit()
    else:
        print str(n) + ' meters = ' + str(b) + ' decimeter(s)'
        quit()

def meter():
    try:
        a = float(raw_input('How many meters would you like to convert? '))
    except ValueError:
        print 'You need to enter a number!'
        meter()
    b = raw_input('What you you like to convert to? [M]illimeters, [C]entimeters, [D]ecimeters, [K]ilometers: ')
    if b == 'M' or b == 'm':
        meters_millimeters(a)
    elif b == 'C' or b == 'c':
        meters_centimeters(a)
    elif b == 'D' or b == 'd':
        meters_decimeters(a)
    else:
        print 'That unit is not available yet!'
