import sys
def syntaxerror():  
    a = open('calc.out', 'w')
    a.write('Dont Let Me Down')
    a.close()
    sys.exit()

import re
f = open('calc.in', 'r')
fil = f.read()
file = fil.splitlines()  

keywords = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'sifir', 'bir', 'iki', 'uc', 'dort', 'bes', 'alti' , 'yedi', 'sekiz', 'dokuz', 'dogru', 'yanlis', '+', '-', '*', 'arti', 'eksi', 'carpi', 've', 'veya', '(', ')','ac-parantez', 'kapa-parantez', 'AnaDegiskenler', 'YeniDegiskenler', 'Sonuc', 'degeri', 'olsun', 'nokta'}
sayilar = ['sifir', 'bir', 'iki', 'uc', 'dort', 'bes', 'alti', 'yedi', 'sekiz', 'dokuz']
varDeg = '[a-zA-Z0-9]'
intDeg = '[0-9]'
fltDeg = '[0-9]\.[0-9]'
boolDeg = 'dogru'
boolDeg2 = 'yanlis'
olmamali = ['(',')','ac-parantez','kapa-parantez','arti','eksi','carpi','ve','veya','+','-','*']
parantez = ['(',')','ac-parantez','kapa-parantez']
aritop = ['arti','eksi','carpi','+','-','*', 'nokta']
logop = ['ve','veya']
boool=[]
fltsayi = []
for i in range(10):
    for k in range(10):
        i = str(i)
        k= str(k)
        s = i + '.' + k
        fltsayi.append(s)

intnames = []
intlines = []
for i in file: 
    intLine = re.findall('[ ]*'+varDeg+'+[ ]*degeri[ ]*'+intDeg+'[ ]*olsun[ ]*$', i)
    if intLine != []:
        for i in intLine:
            t = i.split()
            intnames.append(t[0])
        intlines.append(intLine[0])
for i in file:
    for k in sayilar:
        intLine = re.findall('[ ]*'+varDeg+'+[ ]*degeri[ ]*'+k+'[ ]*olsun[ ]*$', i)
        if intLine != []:
            intlines.append(intLine[0])

fltnames = []
fltlines = []
for i in file:
    fltLine = re.findall('[ ]*'+varDeg+'+[ ]*degeri[ ]*'+fltDeg+'[ ]*olsun[ ]*$', i)
    if fltLine != []:
        for i in fltLine:
            t = i.split()
            fltnames.append(t[0])
        fltlines.append(fltLine[0])
for i in file:
    for k in sayilar:
        for t in sayilar:
            z = k+' ' + 'nokta'+' '+t
            fltLine = re.findall('[ ]*' + varDeg + '+[ ]*degeri[ ]*' + z + '[ ]*olsun[ ]*$', i)
            if fltLine != []:
                for i in fltLine:
                    t = i.split()
                    fltnames.append(t[0])
                fltlines.append(fltLine[0])

boolnames = []
boollines = []
for i in file:
    boolLine = re.findall('^[ ]*'+varDeg+'+[ ]*degeri[ ]*'+boolDeg+'[ ]*olsun[ ]*$', i)
    if boolLine != []:
        for i in boolLine:
            t = i.split()
            boolnames.append(t[0])
        boollines.append(boolLine[0])
for i in file:
    boolLine = re.findall('^[ ]*'+varDeg+'+[ ]*degeri[ ]*'+boolDeg2+'[ ]*olsun[ ]*$', i)
    if boolLine != []:
        for i in boolLine:
            t = i.split()
            boolnames.append(t[0])
        boollines.append(boolLine[0])

deflines=[]
for i in intlines:
    deflines.append(i)
for i in fltlines:
    deflines.append(i)
for i in boollines:
    deflines.append(i)


if 'AnaDegiskenler' not in file:
    syntaxerror()
if 'YeniDegiskenler' not in file:
    syntaxerror()
if 'Sonuc' not in file:
    syntaxerror()
if file.index('YeniDegiskenler') < file.index('AnaDegiskenler'):
    syntaxerror()
if file.index('Sonuc') < file.index('YeniDegiskenler'):
    syntaxerror()
control = 0 
control2 = 0
control3 = 0
for i in file:
    if i == 'AnaDegiskenler':
     control += 1
    if control > 1:
        syntaxerror()
for i in file:
    if i == 'YeniDegiskenler':
     control2 += 1
    if control2 > 1:
        syntaxerror()
for i in file:
    if i == 'Sonuc':
     control3 += 1
    if control3 > 1:
        syntaxerror()

initstatement = []
midstatement = []
sonucstatement = []
for i in file:
    if i == 'YeniDegiskenler':
        break
    else:
        if i != '' and i != 'AnaDegiskenler':
            initstatement.append(i)
for i in file:
    if i == 'Sonuc':
        break
    else:
        if i not in initstatement and i != '' and i != 'AnaDegiskenler' and i != 'YeniDegiskenler':
            midstatement.append(i)
for i in file:
    if i not in initstatement and i not in midstatement and i != '' and i != 'AnaDegiskenler' and i != 'YeniDegiskenler' and i !='Sonuc':
        sonucstatement.append(i)
for i in initstatement: 
    t = i.split()
    if 'degeri' not in t:
        syntaxerror()
    if 'olsun' not in t:
        syntaxerror()
for i in midstatement:
    t = i.split()
    if 'degeri' not in t:
        syntaxerror()
    if 'olsun' not in t:
        syntaxerror()
for i in sonucstatement:
    t = i.split()
    if 'degeri' in t:
        syntaxerror()
    if 'olsun' in t:
        syntaxerror()

for i in initstatement:
    t = i.split()
    for j in t:
        if j in olmamali:
            syntaxerror()
for i in initstatement:
    if i not in deflines:
        syntaxerror()
varnames = []
vardegs = []
variable = {}

for i in initstatement:
    k = i.split(' ')
    if k[0] in varnames:
        syntaxerror()
    else:
        varnames.append(k[0])
for i in varnames:
    if len(i) > 10:
        syntaxerror()
    if i in keywords:
        syntaxerror()
for i in initstatement: 
    t = re.findall('degeri\s(.*)\solsun',i)[0]
    t = t.split()
    if len(t)>3:
        syntaxerror()
    if len(t) == 3:
        var = t[0]+' ' + t[1] + ' '+t[2]
    if len(t) == 2:
        var = t[0] + t[1]
    if len(t) == 1:
        var = t[0]
    if len(t) == 0:
        var = ' '
    vardegs.append(var)


variable = {}   
for name in varnames:
    for deg in vardegs:
        variable[name] = deg
        vardegs.remove(deg)
        break
#print(variable)
paransay = 0
for i in midstatement: 
    t = re.findall('degeri\s(.*)\solsun',i)[0]
    t = t.split()
    for k in t:
        if k == '(' or k == 'ac-parantez':
            paransay += 1
        elif k == ')' or k == 'kapa-parantez':
            paransay -= 1
if paransay != 0:
    syntaxerror()
sayisal = []
for i in sayilar:
    sayisal.append(i)
for i in aritop:
    sayisal.append(i)
for i in intnames:
    sayisal.append(i)
for i in fltnames:
    sayisal.append(i)
for i in fltsayi:
    sayisal.append(i)
for i in range(10):
    i = str(i)
    sayisal.append(i)

mantiksal = []
for i in boolnames:
    mantiksal.append(i)
for i in logop:
    mantiksal.append(i)
mantiksal.append('dogru')
mantiksal.append('yanlis')

aritsizsayi = []
for i in sayilar:
    aritsizsayi.append(i)
for i in intnames:
    aritsizsayi.append(i)
for i in fltnames:
    aritsizsayi.append(i)
for i in fltsayi:
    aritsizsayi.append(i)

for i in midstatement:
    k = i.split()
    if k[0] in varnames:
        syntaxerror()
    else:
        varnames.append(k[0])

    t = re.findall('degeri\s(.*)\solsun',i)[0]
    t = t.split()
    for k in t:
        if k in varnames:
            continue
        elif k in keywords:
            continue
        elif k in intDeg:    #kontrol et bunu
            continue
        elif k in fltsayi:
            continue
        else:
            syntaxerror()
for i in midstatement:
    t = re.findall('degeri\s(.*)\solsun', i)[0]
    t = t.split()
    for k in t:
        if k in parantez:
            continue
        if k in sayisal:
            for m in t:
                if m in mantiksal:
                    syntaxerror()
        if k in mantiksal:
            for m in t:
                if m in sayisal:
                    syntaxerror()
for i in midstatement:
    t = re.findall('degeri\s(.*)\solsun', i)[0]
    t = t.split()
    for k in range(len(t)):
        if t[k] == '(':
            if t[k+1] == ')':
                syntaxerror()
            if t[k+1] == 'kapa-parantez':
                syntaxerror()
        if t[k] == 'ac-parantez':
            if t[k+1] == ')':
                syntaxerror()
            if t[k+1] == 'kapa-parantez':
                syntaxerror()
for i in midstatement:
    t = re.findall('degeri\s(.*)\solsun', i)[0]
    t = t.split()
    for k in range(len(t)-1):
        if t[k] in aritsizsayi:
            if t[k+1] in aritsizsayi:
                syntaxerror()
    for k in range(len(t)-1):
        if t[k] in aritop:
            if t[k+1] in aritop:
                syntaxerror()
    for k in range(len(t)-1):
        if t[k] in logop:
            if t[k+1] in logop:
                syntaxerror()
    for k in range(len(t)-1):
        if t[k] in boool:
            if t[k+1] in boool:
                syntaxerror()

paransay2 = 0
for i in sonucstatement:
    i = i.split()
    for t in i:
        if t == '(' or t == 'ac-parantez':
            paransay2 += 1
        elif t == ')' or t == 'kapa-parantez':
            paransay2 -= 1
if paransay2 != 0:
    syntaxerror()


for i in varnames:
    alpha = i.isalnum()
    if alpha == False:
        syntaxerror()


a = open('calc.out', 'w')
a.write('Here Comes The Sun')
a.close()
sys.exit()

#print(initstatement)
#print(midstatement)
#print(sonucstatement)



