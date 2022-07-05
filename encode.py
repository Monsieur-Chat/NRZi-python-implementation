txt = open("data_bin.txt","r")
lst = txt.read().split(" ")
txt.close()
t = '1'
s = []
if '1' in lst[-1]:
    lst[-1] = '1'
else :
    lst[-1] = '0'

s.append(t)
for i in range(len(lst)) :
    if lst[i] == '0' :
        s.append(t)
    else :
        if t == '1' :
            t = '-1'
        else :
            t = '1'
        s.append(t)
s = ' '.join(s)

try :
    with open('data_t.txt', 'w') as f:
        f.write(s)
    print("[+] ./data_t.txt was successfully created !")
except :
    print("/!\ Error has occured !")
