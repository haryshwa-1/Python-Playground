def solve(val) :
    number = []
    sign = []

    def process():
        res = ""
        for x in val:
            if 47 < ord(x) < 58 :
                res = res + x
            else:
                if len(res) > 0 :
                    number.append(int(res))
                sign.append(x)
                res = ""
        if len(res) > 0 :
            number.append(int(res))
        if ord(val[0]) == 45:
            sign.pop(0)
            number[0] = -number[0]

    def multi_and_divide():
        n = len(number)
        m = len(sign)
        j = 0
        for i in range(0,m):
            if ord(sign[i]) == 42 :
                number[j] = number[j]*number[j+1]
                number.pop(j+1)
                j -= 1
            if ord(sign[i]) == 47:
                number[j] = int(number[j] / number[j + 1])
                number.pop(j+1)
                j -= 1
            else:
                j += 1


    def add_and_sub():
        n = len(number)
        m = len(sign)
        j = 0
        for i in range(0,m):
            if ord(sign[i]) == 43 :
                number[j] = number[j]+number[j+1]
                number.pop(j+1)
            if ord(sign[i]) == 45:
                number[j] = int(number[j] - number[j + 1])
                number.pop(j+1)

    process()
    multi_and_divide()
    add_and_sub()
    return number[0]