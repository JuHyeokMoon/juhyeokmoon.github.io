def pp(s):
    length = len(s)
    q, r = divmod(length,2)
    if r == 0 :
        return s[q-1:q+1]
    else :
        return s[q]

st = input("")
print(pp(st))