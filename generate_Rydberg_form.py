import pandas as pd
import numpy as np

precise_a = 2
precise_value  = 2

def frange(x, y, step):
    while x < y:
        yield x
        x = round(x+step, precise_a)


def generate_Rydberg(R):
    form = []
    temp = []
    alpha = list(frange(0,1,0.02))
    for i in alpha:
        row = []
        for j in range(1,11):
            # print(i,' ',j)
            row.append(round(R / pow(i + j, 2), precise_value))
        temp.append(row)
    for i in range(len(temp)):
        stop = len(temp[i]) - 1
        row = []
        row.append(alpha[i])
        for j in range(len(temp[i])):
            row.append(temp[i][j])
            if j == stop:
                break
            row.append(round(temp[i][j]-temp[i][j+1], precise_value))
        form.append(row)
    return form


if __name__ == '__main__':
    """
    测试功能是否正确
    """
    R = 109737.31
    form = generate_Rydberg(R)
    print(np.shape(form))
    print(len(form))
    # for i in range(len(form)):
    #     print(i)
    #     print(form[i])

    form = np.array(form)

    cols = ['alpha', '1', '12', '2', '23', '3', '34', '4', '45', '5', '56', '6', '67', '7', '78', '8', '89', '9',
            '9 10', '10']
    # dataFrame储存着里德伯表
    dataFrame = pd.DataFrame(form, columns=cols)
    print(dataFrame)