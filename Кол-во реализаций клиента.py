import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 20)  # расширение области видимости данных таблицы
pd.set_option('display.width', 2000)
n = 0
date_list = [2015, 2016, 2017, 2018, 2019]

years = []
clients = []
sum_ship = []
prof_ship = []
ship_per = []
# clients50 = []
# clients100 = []
# clients300 = []
# clients500 = []

sales = {'year': years,
         'clients': clients,
         'sum_ship': sum_ship,
         'prof_ship': prof_ship,
         'ship_per': ship_per}
# 'clients50': clients50,
# 'clients100': clients100,
# 'clients300': clients300,
# 'clients500': clients500}

for year in date_list:
    df2015 = pd.read_excel(f'{year}.xls')
    years.append(year)
    df2015 = df2015.iloc[14:, [0, 16, 20, 22, 24, 25, 26, 27, 28]]

    df2015.columns = ['docs', 'price_ship', 'sum_ship', 'prof_ship', 'ship_per', 'price_pay', 'sum_pay', 'prof_pay',
                      'pay_per']
    df2015 = df2015[['docs', 'price_ship', 'sum_ship', 'prof_ship', 'ship_per']]
    # df2015 = df2015[df2015.docs.str.contains('Реализация') != True]
    df2015 = df2015[df2015.docs.str.contains('Итого') != True]
    df2015 = df2015.fillna(0)
    df2015 = df2015[df2015.sum_ship != 0]
    for i in df2015.docs:
        if df2015.docs.str.contains('СЕЛЬТА') == True:

