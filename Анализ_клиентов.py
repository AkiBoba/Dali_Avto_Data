import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 20)  # расширение области видимости данных таблицы
pd.set_option('display.width', 2000)
n = 0
date_list = [2015, 2016, 2017, 2018, 2019]

years = []
clients = []
clients0 = []
clients30 = []
clients50 = []
clients100 = []
clients300 = []
clients500 = []

sales = {'year': years,
         'clients': clients,
         'clients0': clients0,
         'clients30': clients30,
         'clients50': clients50,
         'clients100': clients100,
         'clients300': clients300,
         'clients500': clients500}

for year in date_list:
    df2015 = pd.read_excel(f'{year}.xls')
    years.append(year)
    df2015 = df2015.iloc[14:, [0, 16, 20, 22, 24, 25, 26, 27, 28]]

    df2015.columns = ['docs', 'price_ship', 'sum_ship', 'prof_ship', 'ship_per', 'price_pay', 'sum_pay', 'prof_pay',
                      'pay_per']
    df2015 = df2015[['docs', 'sum_ship']]
    df2015 = df2015[df2015.docs.str.contains('Реализация') != True]
    df2015 = df2015[df2015.docs.str.contains('Итого') != True]  #
    df2015 = df2015.fillna(0)
    df2015 = df2015[df2015.sum_ship != 0]
    # Количество клиентов с ротацией по суммам отгрузок
    # clients.append(df2015.docs.count())
    # clients0.append(df2015.sum_ship[df2015.sum_ship < 30000 * 12].count())
    # clients30.append(df2015.sum_ship[(df2015.sum_ship < 50000 * 12) & (df2015.sum_ship >= 30000 * 12)].count())
    # clients50.append(df2015.sum_ship[(df2015.sum_ship < 100000 * 12) & (df2015.sum_ship >= 50000 * 12)].count())
    # clients100.append(df2015.sum_ship[(df2015.sum_ship < 300000 * 12) & (df2015.sum_ship >= 100000 * 12)].count())
    # clients300.append(df2015.sum_ship[(df2015.sum_ship < 500000 * 12) & (df2015.sum_ship >= 300000 * 12)].count())
    # clients500.append(df2015.sum_ship[df2015.sum_ship >= 500000 * 12].count())
    # Сумма отгрузок за год с ротацией по среднемесячным отгрузкам клиентов
    clients.append(df2015.sum_ship.sum())
    clients0.append(df2015.sum_ship[df2015.sum_ship < 30000 * 12].sum())
    clients30.append(df2015.sum_ship[(df2015.sum_ship < 50000 * 12) & (df2015.sum_ship >= 30000 * 12)].sum())
    clients50.append(df2015.sum_ship[(df2015.sum_ship < 100000 * 12) & (df2015.sum_ship >= 50000 * 12)].sum())
    clients100.append(df2015.sum_ship[(df2015.sum_ship < 300000 * 12) & (df2015.sum_ship >= 100000 * 12)].sum())
    clients300.append(df2015.sum_ship[(df2015.sum_ship < 500000 * 12) & (df2015.sum_ship >= 300000 * 12)].sum())
    clients500.append(df2015.sum_ship[df2015.sum_ship >= 500000 * 12].sum())
data_sale = pd.DataFrame(sales)

# print(data_sale)
fig, ax = plt.subplots()  # подготовка графиков
ax.set(title='trading')  # наименование графика

#  Добавляем подписи к осям:
ax.set_xlabel('year')
ax.set_ylabel('count of clients')

ax.tick_params(labelrotation=45)
# plt.bar(data_sale.year + .1, data_sale.clients, width=.1, label=f'clients all')
plt.bar(data_sale.year + .2, data_sale.clients0, width=.1, label=f' < 30 000 in month')
plt.bar(data_sale.year + .3, data_sale.clients30, width=.1, label=f' >= 30 000 in month')
plt.bar(data_sale.year + .4, data_sale.clients50, width=.1, label=f' >= 50 000 in month')
plt.bar(data_sale.year + .5, data_sale.clients100, width=.1, label=f' >= 100 000 in month')
plt.bar(data_sale.year + .6, data_sale.clients300, width=.1, label=f' >= 300 000 in month')
plt.bar(data_sale.year + .7, data_sale.clients500, width=.1, label=f' >= 500 000 in month')
# ax.text(2017, 500, 'всего клиентов')
#
# ax.text(2017, 300, 'клиенты от 30 тр')

ax.legend()
fig.set_figwidth(12)
fig.set_figheight(12)
print(data_sale)
# plt.show()
