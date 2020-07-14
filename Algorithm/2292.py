#2292 벌집

num = int(input(''))

root = 1
cnt_six = 6
count = 1

while num > count :
    root += 1
    count += cnt_six
    cnt_six += 6
    
print(f'{root}')
