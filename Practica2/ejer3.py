list = ['Auto', '123', 'Viaje', '50', '120']
list_num = []

for i in list:
    if i.isdecimal():
        list_num.append(int(i))
list_num.sort()

print(list_num)

