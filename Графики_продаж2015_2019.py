# Построение графиков продаж в 2015 - 2019 годах с разбивкой на 12 месяцев

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 20)  # расширение области видимости данных таблицы
pd.set_option('display.width', 2000)


def year(year):
    df2015 = pd.read_excel(f'{year}.xls')

    df2015 = df2015.iloc[11:, [0, 16, 20, 22, 24, 25, 26, 27, 28]]

    df2015.columns = ['docs', 'price_ship', 'sum_ship', 'prof_ship', 'ship_per', 'price_pay', 'sum_pay', 'prof_pay',
                      'pay_per']

    df2015 = df2015[df2015.docs.str.contains('Реализация') == True]
    df2015.index = [n for n in range(len(df2015))]
    for i in range(len(df2015)):
        string = df2015.docs[i][45:47]
        df2015.docs[i] = string

    df2015 = df2015[['docs', 'sum_ship']]
    df2015 = df2015.groupby('docs').sum()[['sum_ship']]  # agg({'sum_ship': 'sum'})

    return df2015


date_list = [2015, 2016, 2017, 2018]
fig, ax = plt.subplots()  # подготовка графиков
ax.set(title='trading')  # наименование графика

#  Добавляем подписи к осям:
ax.set_xlabel('месяц')
ax.set_ylabel('сумма продаж, 10*млн. руб')
X = pd.DataFrame([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
k = 1
for i in date_list:
    # plt.bar(X[0] + .2 * k, year(i)['sum_ship'], width=.2, label=f'{i} year')
    plt.subplot(len(date_list), 1, k)
    plt.plot(X[0], year(i)['sum_ship'], label=f'{i} year')
    plt.grid()
    k += 1

ax.legend()
fig.set_figwidth(12)
fig.set_figheight(12)
plt.show()
