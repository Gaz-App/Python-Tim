age = 50

"""
print ('Mi edad es de: ' + age + ' años')
TypeError: can only concatenate str (not "int") to str
"""

print('Mi edad es de: ' + str(age) + ' años')

print('-----OTHER WAY:')

print('Mi edad es de {} años'.format(age))

print('----------------------->')

print('There are {0} days in {1},{2},{3},{4},{5},{6},{7}'
      .format(31, 'ENE ', 'MAR ', 'MAY ', 'JUL ', 'AGO ', 'OCT ', 'DEC'))

print('There are {0} days in ENE, MAR, MAY, JUL, AGO, OCT, DEC'.format(31))

print('ENE: {2}, FEB: {0}, MAR: {2}, ABR: {1}, MAY: {2}, JUN: {2},'
      ' JUL: {2}, SEP: {1}, OCT: {2}, NOV: {1}, DEC: {2}'.format(28, 30, 31))

print(
    """
ENE: {2}
FEB: {0}
MAR: {2}
ABR: {1}
MAY: {2}
JUN: {2}
JUL: {2}
SEP: {1}
OCT: {2}
NOV: {1}
DEC: {2}
""".format(28, 30, 31))
