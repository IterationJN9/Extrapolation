import math

def extrapolation(start, stop, initial, func, tolerance, max, min):
    nk = [2, 4, 6, 8, 12, 16, 24, 32]
    t_out = start
    estimate_out = initial
    h = max
    flag = 1
    q = [[0 for m in range(7)] for n in range(7)]
    y = [0 for m in range(9)]
    for i in range(0,6):
        for j in range(0,i):
            ratio = nk[i + 1]/nk[j]
            q[i][j] = pow(ratio, 2)
    while flag == 1:
        k = 0
        nflag = 0
        while (k <= 7 and nflag == 0):
            hk = h / nk[k]
            t = t_out
            estimate2 = estimate_out
            estimate3 = estimate2 + (hk * func(t, estimate2))
            t = t_out + hk
            for j in range(0, nk[k] - 2):
                estimate1 = estimate2
                estimate2 = estimate3
                estimate3 = estimate1 + (2 * hk * func(t, estimate2))
                t = t_out + (j + 1) * hk
            y[k] = (estimate3 + estimate2 + hk * func(t, estimate3)) / 2
            if (k >= 1):
                j = k
                v = y[0]
                while (j >= 1):
                    y[j-1] = y[j] + (y[j] - y[j - 1]) / (q[k - 1][j - 1] -1)
                    j = j - 1
                    if (abs(y[0] - v) <= tolerance):
                        nflag = 1
            k = k + 1
        k = k - 1
        if (nflag == 0):
            h = h / 2
            if (h < min):
                print("Minimum exceeded.")
                flag = 0
        else:
            estimate_out = y[0]
            t_out = t_out + h
            if (t_out >= stop):
                flag = 0
                print("Flag set to 0.")
                return estimate_out
            elif (t_out + h > stop):
                h = stop - t_out
            elif (k <= 2 and h < 0.5 * max):
                h = 2 * h
 
print('Enter endpoints: ')
start = float(input('a: '))
stop = float(input('b: '))
initial = float(input('Enter the initial condition: '))
tolerance = float(input('Enter the tolerance: '))
maximum = float(input('Enter the maximum step size: '))
minimum = float(input('Enter the minimum step size: '))
output = extrapolation(start, stop, initial, lambda x, y: y - pow(x,2) + 1, tolerance, maximum, minimum)
print('Check')
print('Result: {0}' .format(output))