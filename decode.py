txt = open("data_t.txt","r")
lst = txt.read().split(" ")
txt.close()

if '-1' in lst[-1]:
    lst[-1] = '-1'
else :
    lst[-1] = '1'

out = ""
prev = ''
for i in lst:
    if prev == '':
        prev = i
    else:
        if i == prev:
            out += '0'
            prev = i
        else:
            out += '1'
            prev = i

try :
    with open('data_bin.txt', 'w') as f:
        f.write(out)
    print("[+] ./data_bin.txt was successfully created !")
except :
    print("/!\ Error has occured !")
