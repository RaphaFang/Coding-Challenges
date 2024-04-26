def sumOfArithmeticSequence(min, max, differ):
    time = int((max-min)/differ)
    list = [min+n*differ for n in range(time+1)]
    return sum(list)

sumOfArithmeticSequence(10,14,3)
