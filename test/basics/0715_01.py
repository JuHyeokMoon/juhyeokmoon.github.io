#closure

def outer_func(tag):

    def inner_func(txt):
        text = txt
        print('<{0}>{1}<{0}>'.format(tag, text))

    return inner_func

h1_func = outer_func('h1')
p_func = outer_func('p')

h1_func('h1태그의 안입니다.')
p_func('p태그의 안입니다.')