def tuple_ss(l):
    #리스트 화 데이터 분리 replace 함수
    l = l[1:length-1].split(',')
    result = [int(i) for i in l[-1]]
    return result

if __name__ == "__main__":
    ts = input("중복없는 튜블의 집합 형태 입력 :")
    print(tuple_ss(ts))