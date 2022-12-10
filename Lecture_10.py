# Даны заработные платы бухгалтеров, юристов и программистов.
# Бухгалтера: 70, 50, 65, 60, 75, 67, 74
# Юристы: 80, 74, 90, 70, 75, 65, 85
# Программисты: 148, 142, 140, 150, 160, 170, 155
# Провести дисперсионный анализ


import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

y1 = np.array([70, 50, 65, 60, 75, 67, 74])
y2 = np.array([80, 74, 90, 70, 75, 65, 85])
y3 = np.array([148, 142, 140, 150, 160, 170, 155])

k = 3
n = 21

y_mean_1 = np.mean(y1)  # среднее значение 1 выборки
y_mean_2 = np.mean(y2)
y_mean_3 = np.mean(y3)


total = [*y1, *y2, *y3]  # объеденим массивы в один

y_mena_total = np.mean(total)  # среднее значение 3-ёх выборок

# Сумма квадратов отклонений средних групповых значений от общего среднего:
S_f = np.sum((y_mean_1-y_mena_total)**2)*7 + np.sum((y_mean_2 -
                                                     y_mena_total)**2)*7+np.sum((y_mean_3-y_mena_total)**2)*7

# Остаточная сумма квадратов отклонений:
S_ost = np.sum((y1-y_mean_1)**2)+np.sum((y2-y_mean_2)**2) + \
    np.sum((y3-y_mean_3)**2)

# Сумма квадратов отклонений наблюдений от общего среднего:
S_1 = np.sum((total-y_mena_total)**2)
# S_1 = S_f + S_ost

# Расчитаем факторную дисперсию:
D_f = S_f/(k-1)

# Расчитаем остаточную дисперсию:
D_ost = S_ost/(n-k)

# Расчитаем наблюдаемый критерий Фишера:
F_n = D_f/D_ost # statistik

# Расчёт с помощью функции:
print(stats.f_oneway(y1, y2, y3))
# Нашли статистически значимые различия, т.к. pvalue < a

# Определим между какими средними арифметическими есть среднестатистические значимы различия:
# Post hoc test Tukey
import pandas as pd
import numpy as np
from scipy. stats import f_oneway
from statsmodels. stats.multicomp import pairwise_tukeyhsd

df = pd.DataFrame({'score': [70,  50,  65,  60,  75,  67,  74,
 80,  74,  90,  70,  75,  65,  85,
 148, 142, 140, 150, 160, 170, 155],
 'group': np.repeat(['accauntant','lawyer','programmer'], repeats= 7 )}) 

# perform Tukey's test
tukey = pairwise_tukeyhsd(endog=df['score'],
 groups=df['group'],
 alpha= 0.05 )

#display results
print(tukey)
# p-adj(pvalue) двух пар accauntant programmer и lawyer programmer < 0.05,
# поэтому делаем вывод что профессия влияет на зп


24:00


