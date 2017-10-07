import pandas as pd
import numpy as np
import generate_Rydberg_form

R = 109737.31
form = generate_Rydberg_form.generate_Rydberg(R)
form = np.array(form)

cols = ['alpha','1','12','2','23','3','34','4','45','5','56','6','67','7','78','8','89','9','9 10','10']
# dataFrame储存着里德伯表
dataFrame = pd.DataFrame(form, columns=cols)


def convert_to_wave_number(lamb):
    return round(pow(10,7)/lamb, 2)


def find_alpha(delta,col):
    """
    根据求得的alpha值等来求出当前对应的alpha值
    :param delta:
    :param m1:
    :param m2:
    :return:
    """
    big_a = find_alpha_bigger_than_delta(delta, col)
    small_a = find_alpha_smaller_than_delta(delta, col)
    big_delta = find_bigger_delta(delta, col)
    small_delta =find_smaller_delta(delta, col)
    alpha = round(big_a + (big_delta - delta)/(big_delta-small_delta)*(small_a - big_a), 3)
    return alpha


def find_alpha_bigger_than_delta(delta, col):
    """
    这个函数的主要功能是找出比当前delta值大的最近的里德伯表那一行对应的alpha值
    :param delta:
    :param col:
    :return:
    """
    result = list(dataFrame[dataFrame[col] > delta]['alpha'])
    return result[-1]


def find_alpha_smaller_than_delta(delta, col):
    """
    这个函数的主要功能是找出比当前delta值小的最近的里德伯表那一行对应的alpha值
    :param delta:
    :param col:
    :return:
    """
    result = list(dataFrame[dataFrame[col] < delta]['alpha'])
    return result[0]


def find_bigger_delta(delta, col):
    """
    这个函数的主要功能是找出比当前delta值大的最近delta值
    :param delta:
    :param col:
    :return:
    """
    result = list(dataFrame[dataFrame[col] > delta][col])
    return result[-1]


def find_smaller_delta(delta, col):
    """
     这个函数的主要功能是找出比当前delta值小的最近delta值
    :param delta:
    :param col:
    :return:
    """
    result = list(dataFrame[dataFrame[col] < delta][col])
    return result[0]


def find_n(lambda1, lambda2):
    """
    这个函数的主要作用是找出最大的波长对应的n值
    :param lambda1:
    :param lambda2:
    :return:
    """
    lambda_max = max(lambda1, lambda2)
    lambdas = [589, 475, 515, 615, 467, 497, 568]
    ns = {0: 3, 1: 7, 2: 6, 3: 5, 4: 6, 5: 5, 6: 4}
    for i in range(len(lambdas)):
        scope = 2
        if lambda_max >= lambdas[i] - scope and lambda_max <= lambdas[i] + scope:
            n = i
            break
    n = ns[n]
    return n


def find_delta_l(n,m,alpha):
    """
    根据已知的m,n,alpha求对应的delta_l值
    :param n:
    :param m:
    :param alpha:
    :return:
    """
    return round(n - m - alpha, 3)


def find_which_col(delta):
    """
    根据delta值求出所在的列
    :param delta:
    :return:
    """

    cols = ['12','23','34','45','56','67','78','89']
    for col in cols:
        l = list(dataFrame[col])
        if delta > l[-1] and delta < l[0]:
            return col


def find_m(col):
    """
    根据delta所在的col值提取出较小的m值
    :param col:
    :return:
    """
    m = int(col)
    m = m // 10
    return m

def find_fixed_term(wave_number, R, n, delta_l):
    """
    根据波数，常熟，n值还有delta_l求出固定项
    :param wave_number:
    :param R:
    :param n:
    :param delta_l:
    :return:
    """
    result = round(wave_number + R / pow(n-delta_l, 2), generate_Rydberg_form.precise_value)
    return round(result, 2)

if __name__ == '__main__':
    """
    测试功能是否正确
    """
    lambda1 = 330.266
    lambda2 = 285.293

    wave_number1 = convert_to_wave_number(lambda1)
    wave_number2 = convert_to_wave_number(lambda2)

    delta = round(abs(wave_number1 - wave_number2), generate_Rydberg_form.precise_value)
    print("delta:",delta)
    col = find_which_col(delta)
    alpha = find_alpha(delta, col)
    print("alpha:",alpha)
    n = 4
    m = find_m(col)
    print("m",m)
    delta_l = find_delta_l(n,m,alpha)
    print("delta_l",delta_l)

    lambda_max = max(lambda1, lambda2)
    wave_number = convert_to_wave_number(lambda_max)
    R = 109737.31
    fixed_term = find_fixed_term(wave_number, R, n, delta_l)
    print("fixed_term",fixed_term)
