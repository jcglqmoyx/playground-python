file = open('/home/jcglqmoyx/Desktop/1.txt', 'r', encoding='utf-16')
content = file.readlines()
simple = input('Input a simple Chinese character: ')
flag = True
res = simple
for line in content:
    if simple in line:
        res = line[1]
        print(res)
        flag = False
        break
if flag:
    print(simple)

hangul_file = open('/home/jcglqmoyx/Desktop/hangul.txt', 'r')
cnt = hangul_file.readlines()
for l in cnt:
    if res in l:
        print(l[0])
        break
