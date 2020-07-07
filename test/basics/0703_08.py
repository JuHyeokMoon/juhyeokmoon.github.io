
input = open("test/test_file.txt",'r',encoding='utf-8')
inStr = ''
inStr2 = ''
while 1 :
    inStr = input.readline()
    inStr2 = inStr2 + inStr
    if inStr =='':
        break
    print(inStr, end='')
print(inStr2)

input.close()