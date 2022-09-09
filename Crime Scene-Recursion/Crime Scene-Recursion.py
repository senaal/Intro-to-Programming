file = open('crime_scene.txt', 'r')
scene = file.read()
crime_scene = scene.split()
W = int(crime_scene[0])
T = int(crime_scene[1])
N = int(crime_scene[2])
evidences = scene.splitlines()
evidences.pop(0)
evidences.pop(0)
#print(crime_scene)
#print(evidences)
ids = []
weights = []
times = []
values = []
for i in evidences:
    i = i.split()
    ids.append(int(i[0]))
    weights.append(int(i[1]))
    times.append(int(i[2]))
    values.append(int(i[3]))


def sortf(list):
    if len(list) <= 1:
        return list
    i = 1
    j = len(list) - 1
    while True:
        if j < i:
            break
        if list[i] <= list[0]:
            i += 1
            continue
        elif list[j] >= list[0]:
            j -= 1
            continue
        list[i], list[j] = list[j], list[i]

    list[0], list[j] = list[j], list[0]
    list[0:j] = sortf(list[0:j])
    list[j+1:] = sortf(list[j + 1:])
    return list


def f1(limit, i):
    if i == N:
        return 0, []
    if limit - weights[i] >= 0:
        col_val, col_list = f1(limit - weights[i], i+1)
        col_val += values[i]
        col_list.append(ids[i])
    else:
        col_val = 0
        col_list = []
    col_val_not, col_list_not = f1(limit, i+1)
    sortf(col_list)
    sortf(col_list_not)
    if col_val > col_val_not:
        return col_val, col_list
    else:
        return col_val_not, col_list_not

sol1 = open('solution_part1.txt', 'w')
a = str(f1(W, 0)[0])
b = (f1(W, 0)[1])
sol1.write(a)
sol1.write('\n')
for i in b:
    i = str(i)
    sol1.write(i)
    sol1.write(' ')
sol1.close()
#print(f1(W,0))

def f2(limit, i):
    if i == N:
        return 0, []
    if limit - times[i] >= 0:
        col_val, col_list = f2(limit - times[i], i+1)
        col_val += values[i]
        col_list.append(ids[i])
    else:
        col_val = 0
        col_list = []
    col_val_not, col_list_not = f2(limit, i+1)
    sortf(col_list)
    sortf(col_list_not)
    if col_val > col_val_not:
        return col_val, col_list
    else:
        return col_val_not, col_list_not

sol2 = open('solution_part2.txt', 'w')
a = str(f2(T, 0)[0])
b = (f2(T, 0)[1])
sol2.write(a)
sol2.write('\n')
for i in b:
    i = str(i)
    sol2.write(i)
    sol2.write(' ')
sol2.close()
#print(f2(T,0))

def f3(limit1,limit2, i):
    if i == N:
        return 0, []
    if limit1 - weights[i] >= 0 and limit2 - times[i] >= 0:
        col_val,  col_list = f3(limit1-weights[i], limit2 - times[i], i+1)
        col_val += values[i]
        col_list.append(ids[i])
    else:
        col_val = 0
        col_list = []
    col_val_not, col_list_not = f3(limit1, limit2, i+1)
    sortf(col_list)
    sortf(col_list_not)
    if col_val > col_val_not:
        return col_val, col_list
    else:
        return col_val_not, col_list_not

sol3 = open('solution_part3.txt', 'w')
a = str(f3(W, T, 0)[0])
b = (f3(W, T, 0)[1])
sol3.write(a)
sol3.write('\n')
for i in b:
    i = str(i)
    sol3.write(i)
    sol3.write(' ')
sol3.close()
#print(f3(W, T, 0))
file.close()
#recursion fonksiyonları yazarken lab sessionından faydalandım.