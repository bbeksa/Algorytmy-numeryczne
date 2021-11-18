def newtons_polynomial_interpolation(xlist=None, ylist=None):
    if ylist is None:
        ylist = []
    if xlist is None:
        xlist = []
    if len(xlist) != len(ylist):
        raise Exception("Listy argumentów muszą być równe!")

    result = []

    for i in range(0, len(xlist)):
        result.append(0)

    blist = []

    for i in range(0, len(xlist)):
        blist.append(determine_bn(xlist, ylist, i))

    for i in range(1, len(xlist)):
        tmp = [1, -xlist[i - 1]]
        for j in range(1, i):
            tmp = multiply_polynomials(tmp, [1, -xlist[j - 1]])
        tmp = multiply_polynomial(tmp, blist[i])
        result = add_polynomials(result, tmp)

    result[len(result) - 1] += blist[0]

    return result


def determine_bn(xlist, ylist, n):
    result = 0
    for j in range(0, n+1, 1):
        denominal = 1
        for i in range(0, n+1, 1):
            if i != j:
                denominal *= (xlist[j] - xlist[i])
        result += ylist[j]/denominal
    return result


def add_polynomials(input1=None, input2=None):
    if input2 is None:
        input2 = []
    if input1 is None:
        input1 = []
    if len(input1) <= len(input2):
        n = len(input1)
        result = input2
    else:
        n = len(input2)
        result = input1

    input1.reverse()
    input2.reverse()
    for i in range(0, n):
        result[i] = input1[i] + input2[i]

    result.reverse()
    return result


def multiply_polynomials(input1=None, input2=None):
    if input2 is None:
        input2 = []
    if input1 is None:
        input1 = []
    result = []

    for i in range(0, len(input1) + len(input2) - 1):
        result.append(0)

    for i in range(0, len(input1)):
        for j in range(0, len(input2)):
            result[i + j] = result[i + j] + input1[i] * input2[j]

    return result


def multiply_polynomial(input1=None, x=0):
    if input1 is None:
        input1 = []
    result = []

    for i in range(0, len(input1)):
        result.append(input1[i] * x)

    return result
