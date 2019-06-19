from calculadora import *

with open("operaciones.txt",'rU') as f:
    content = f.readlines()

cal = Calculadora()

for i in content:
    content = i.strip('\n').split(' ')
    print(cal.pos_orden(content))
