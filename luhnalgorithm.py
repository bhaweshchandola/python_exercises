x = list(input())
check = x[-1]

intx = list(map(int, x[:-1]))
rev_intx = intx[::-1]

for x1,y1 in enumerate(rev_intx):
    if x1%2==0:
        rev_intx[x1] *= 2

        if rev_intx[x1]>9:
            rev_intx[x1] = sum(list(map(int, list(str(rev_intx[x1])))))


sum_x = str(sum(rev_intx)*9)[-1]
print(sum_x)
print(check)

# 4929783006273701
# 6011024611353792
# algorithm to check card number validity





