import random
import matplotlib.pyplot as plt
import numpy as np


def limitShape(u):
    return (2/np.pi)*(u*np.arcsin(u/np.sqrt(2)) + np.sqrt(2-u**2))

def generate_random_word(n,k):
    result = []
    for i in range(1,n+1):
        result += [i] * k

    result_list = result
    random.shuffle(result_list)

    return result_list

def rsk(w):
    tableau = []
    for i in range(len(w)):
        row = 0
        bumped = w[i]
        while(True):
            if row == len(tableau):
                tableau.append([bumped])
                break
            bumpedPrev = bumped
            for j in range(len(tableau[row])):
                if bumped < tableau[row][j]:
                    bumped = tableau[row][j] 
                    tableau[row][j] = bumpedPrev
                    break
            if bumped == bumpedPrev:
                tableau[row]+=[bumpedPrev]
                break
            row += 1
        
        if i % (len(w)//10) == 0:
            print(f"At {100*i/len(w)}%")
        
    return tableau

def rot(x,y):
    theta = np.radians(45)

    x_rotated = x * np.cos(theta) - y * np.sin(theta)
    y_rotated = x * np.sin(theta) + y * np.cos(theta)
    return x_rotated,y_rotated

def rotBack(x,y):
    theta = np.radians(-135)

    x_rotated = x * np.cos(theta) - y * np.sin(theta)
    y_rotated = x * np.sin(theta) + y * np.cos(theta)
    return x_rotated,y_rotated


# Example usage
# n=20
# k = 20

d = {}
samples = 100

nk = 50000


def kfunc(n, slope, intercept):
    return int(slope*n + intercept)


slope = 0.2
intercept = 15
# n_values = [10, 30, 60, 120, 240, 580, 800, 1000, 1500, 2000]
n_values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20,30,40,50,60,70,80,90,100,240, 400, 580, 700]#, 800, 1000, 1500, 2000, 2250, 2500, 2750, 3000, 3250, 3500]
k_values = []

for nn in n_values:
    k_values += [kfunc(nn, slope, intercept)]

print(n_values)
print(k_values)


# for i in range(len(n_values)):
#     t = int(np.sqrt(nk/(n_values[i]*k_values[i])))
#     n_values[i] *= t
#     k_values[i] *= t

# for i in range(samples):
#     w = generate_random_word(n,k)
#     if str(w) not in d:
#         d[str(w)] = 1
#     else:
#         d[str(w)] += 1

# for word, count in d.items():
#     print(f"{word}: has probability {count/samples}")

# print(len(d))


firstRowXList = []
firstRowYList = []
lastRowXList = []
lastRowYList = []
ratioList = []


for n, k in zip(n_values, k_values):
    print(n,k)
    # n += ite*100
    # k += ite*50
    w = generate_random_word(n,k)
    P = rsk(w)

    dataX = []
    dataY = []

    dataX += [0]
    dataY += [0]
    firstRowY = 0
    firstRowX = 0
    lastRowY = 0
    lastRowX = 0
    for i in range(len(P)):
        tmpX1 = i/((n*k)**0.5)
        tmpX2 = (i+1)/((n*k)**0.5)
        tmpY1 = len(P[i])/((n*k)**0.5)
        tmpY2 = len(P[i])/((n*k)**0.5)
        rX1, rY1 = rot(tmpX1, tmpY1)
        rX2, rY2 = rot(tmpX2, tmpY2)
        dataX += [rX1]
        dataX += [rX2]
        dataY += [rY1]
        dataY += [rY2]
        if i == 0:
            firstRowY = rY1
            firstRowX = rX1


    tmpX1 = len(P)/((n*k)**0.5)
    tmpY1 = 0
    rX1, rY1 = rot(tmpX1, tmpY1)
    lastRowX = rX1
    lastRowY = rY1
    dataX += [rX1]
    dataY += [rY1]
    dataX += [0]
    dataY += [0]
    (rfirstRowX, rfirstRowY) = rotBack(firstRowX, firstRowY)
    (rlastRowX, rlastRowY) = rotBack(lastRowX, lastRowY)

    firstRowXList += [rfirstRowX]
    firstRowYList += [rfirstRowY]
    lastRowXList += [rlastRowX]
    lastRowYList += [rlastRowY]
    ratioList += [n]

    # plt.plot(dataX,dataY)
 
    # if ite % (samples//10) == 0:
        # print(f"At {100*ite/samples}%")


# firstRowXAv = sum(firstRowXList) / len(firstRowXList)
# firstRowYAv = sum(firstRowYList) / len(firstRowYList)
# lastRowXAv = sum(lastRowXList) / len(lastRowXList)
# lastRowYAv = sum(lastRowYList) / len(lastRowYList)

# print("first row av:", round(firstRowXAv, 5), round(firstRowYAv,5))
# print("last row av:", round(lastRowXAv,5), round(lastRowYAv,5))

# x_values = np.linspace(-np.sqrt(2)+0.000001, np.sqrt(2)-0.000001, 100)
# y_values = limitShape(x_values)
# plt.plot(x_values, y_values, c="black", linewidth=2.5)

plt.scatter(ratioList, firstRowXList, color="blue",s=8.2, label="horizontal distance")
plt.scatter(ratioList, lastRowYList, color="red",s=8.2, label="vertical distance")

miR = min(n_values)
maR = max(n_values)

plt.xscale('log')
plt.xlabel('n')
plt.ylabel('distance')
plt.title('Two Scatter Plots in One Figure')
plt.legend()
plt.savefig(f"nVdistance_nvals{miR}-{maR}_slope{slope}_intercept{intercept}.png", dpi=600)
plt.show()