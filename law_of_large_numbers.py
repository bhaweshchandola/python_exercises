from numpy.random import randn

def gen(n):
    counter = 0
    for x in randn(n):
        if -1<x<1:
            counter += 1

    return counter/n


print(gen(1000000))

# n=10 => 0.69
# n=100 => 0.666
# n=1000 => 0.678
# n=10000 => 0.68237
# n=100000 => 0.682694
# since randn produces number from normal distribution then it is proved that number between -1 and 1 is actuall 68.2 percent

''' testing law of large numbers i.e. if we average out the values of a given scenario then it will gives us the expected values when number of instances reaches infinity or a large number'''