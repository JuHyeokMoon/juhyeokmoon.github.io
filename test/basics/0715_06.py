#연습문제2
#핸드폰 번호 가리기 문제


def handphone(number):
    length = len(number)
    result = number.replace(number[:7],'*'*length)
    # print(f'orgin : {number}, return : ********{number[-4:]}')
    print(result)

if __name__ == "__main__":
    num = input("enter phone number >>")
    handphone(num)




