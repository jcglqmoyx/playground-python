chinese = input('Input your Chinese name: ')
tradition, korean = '', ''
for ch in chinese:
    file = open('/home/jcglqmoyx/projects/pycharm-projects/playground-python/src/api/name_conversion/comparison.txt', 'r', encoding='utf-8')
    content = file.readlines()
    flag = True
    res = ch
    for line in content:
        if ch in line:
            res = line[1]
            tradition += res
            flag = False
            break
    if flag:
        tradition += ch

    hangul_file = open('/home/jcglqmoyx/projects/pycharm-projects/playground-python/src/api/name_conversion/hangul.txt', 'r')
    cnt = hangul_file.readlines()
    for l in cnt:
        if res in l:
            korean += l[0]
            break
print('Your name in traditional Chinese is: ', tradition)
print('Your name in Korean is ', korean)
