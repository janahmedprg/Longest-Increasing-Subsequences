import random
import matplotlib.pyplot as plt
import numpy as np


def limitShape(u):
    return (2/np.pi)*(u*np.arcsin(u/np.sqrt(2)) + np.sqrt(2-u**2))

def limitShapeConj(c,u):
    return (2/np.pi)*(u*np.arcsin((u+c)/(2*np.sqrt(1+u*c)))+ (1/c)*np.arccos((2+u*c-c*c)/(2*np.sqrt(1+u*c))) + (1/2)*np.sqrt(4-(u-c)**2))

def limitShape2(u):
    return (2/np.pi)*(u*np.arcsin(u/2) + np.sqrt(4-u**2))

def limitShape3(c,u):
    return (np.sqrt(2)/np.pi)*(2/np.sqrt(2) * u*np.arcsin((2/np.sqrt(2)*u+c)/(2*np.sqrt(1+2/np.sqrt(2)*u*c))) + 1/c*np.arccos((2+2/np.sqrt(2)*u*c-c*c)/(2*np.sqrt(1+2/np.sqrt(2)*u*c)))+ 1/2*np.sqrt(4-(2/np.sqrt(2)*u-c)**2))

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

def rot135(x,y):
    theta = np.radians(135)

    x_rotated = x * np.cos(theta) - y * np.sin(theta)
    y_rotated = x * np.sin(theta) + y * np.cos(theta)
    return x_rotated,y_rotated


# Example usage
n = 30
k = 100

d = {}
samples = 1

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
lastRowYList = []
for ite in range(samples):
    # n += ite*100
    # k += ite*50
    w = generate_random_word(n,k)
    P = rsk(w)

    dataX = []
    dataY = []

    dataX += [0]
    dataY += [0]
    firstRowX = 0
    firstRowY = 0
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
            firstRowX = rX1
            firstRowY = rY1


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
    lastRowYList += [rlastRowY]

    plt.plot(dataX,dataY)

    # if ite % (samples//10) == 0:
        # print(f"At {100*ite/samples}%")

c = np.sqrt(k/n)
firstRowXAv = sum(firstRowXList) / len(firstRowXList)
lastRowYAv = sum(lastRowYList) / len(lastRowYList)
print("avs:", firstRowXAv, lastRowYAv)
x_values = np.linspace(c-2+0.000001, c+2-0.000001, 100)
# y_values = limitShape(x_values)
y_values = limitShape3(c,x_values)
# y_values = limitShape2(x_values)
# x_scaled = []
# y_scaled = []

# for i in range(len(x_values)):
#     xtmp, ytmp = rotBack(x_values[i],y_values[i])
#     tmpX = xtmp
#     xtmp *= firstRowXAv/2
#     ytmp *= lastRowYAv/(-2)
#     ytmp -= 0*np.e**(2-tmpX)*np.sin(-np.pi/2*(tmpX-2))

#     rxtmp, rytmp = rot135(xtmp,ytmp)

#     x_scaled += [rxtmp]
#     y_scaled += [rytmp]


plt.plot(-x_values, y_values, c="black", linewidth=2.5)

plt.axis('equal')
# plt.savefig(f"./k30/n{n}_k{k}_samples{samples}.png", dpi=600)
# plt.clf()
plt.show()