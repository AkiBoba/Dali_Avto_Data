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
    df2015 = df2015[df2015.docs.str.contains('Реализация') != True]
    df2015 = df2015[df2015.docs.str.contains('Итого') != True]  #
    df2015 = df2015.fillna(0)
    df2015 = df2015[df2015.sum_ship != 0]
    # print(f'{year}', df2015.docs.count())
    clients.append(df2015.docs[df2015.docs.str.contains('СЕЛЬТА') == True].item())
    sum_ship.append(df2015.sum_ship[df2015.docs.str.contains('СЕЛЬТА') == True].item())
    prof_ship.append(df2015.prof_ship[df2015.docs.str.contains('СЕЛЬТА') == True].item())
    ship_per.append(df2015.ship_per[df2015.docs.str.contains('СЕЛЬТА') == True].item())
    # clients50.append(df2015.sum_ship[(df2015.sum_ship < 100000 * 12) & (df2015.sum_ship >= 50000 * 12)].sum())
    # clients100.append(df2015.sum_ship[(df2015.sum_ship < 300000 * 12) & (df2015.sum_ship >= 100000 * 12)].sum())
    # clients300.append(df2015.sum_ship[(df2015.sum_ship < 500000 * 12) & (df2015.sum_ship >= 300000 * 12)].sum())
    # clients500.append(df2015.sum_ship[df2015.sum_ship >= 500000 * 12].sum())
    # clients0.append(df2015.docs.count())
    # print(sales['clients0']+sales['clients30']+sales['clients50']+sales['clients100']+sales['clients300']+sales['clients500'])
data_sale = pd.DataFrame(sales)

# print(data_sale)
fig, ax = plt.subplots(2, 1)  # подготовка графиков
# ax.set(title='trading')  # наименование графика

#  Добавляем подписи к осям:
# ax.set_xlabel('year')
# ax.set_ylabel('суммы отгрузок, 10*млн. руб.')

# ax.tick_params(labelrotation=45)
# графики - свечи
# plt.bar(data_sale.year + .1, data_sale.clients, width=.1, label=f'clients all')
plt.subplot(311)
plt.plot(data_sale.year, data_sale.sum_ship, label=f'сумма отгрузок')
plt.grid()
plt.subplot(312)
plt.plot(data_sale.year, data_sale.prof_ship, label=f'Прибыль по отгрузке')
plt.grid()
plt.subplot(313)
plt.plot(data_sale.year, data_sale.ship_per, label=f'Процент наценки по отгрузке')
# plt.bar(data_sale.year + .5, data_sale.clients100, width=.1, label=f' >= 100 000 in month')
# plt.bar(data_sale.year + .6, data_sale.clients300, width=.1, label=f' >= 300 000 in month')
# plt.bar(data_sale.year + .7, data_sale.clients500, width=.1, label=f' >= 500 000 in month')
# графики - линейные
# plt.plot(data_sale.year + .1, data_sale.clients, label=f'clients all')
# plt.plot(data_sale.year, data_sale.clients0, linewidth=5, label=f' < 30 000 in month')
# plt.plot(data_sale.year, data_sale.clients30, linewidth=5, label=f' >= 30 000 in month')
# plt.plot(data_sale.year, data_sale.clients50, linewidth=5, label=f' >= 50 000 in month')
# plt.plot(data_sale.year, data_sale.clients100, linewidth=5, label=f' >= 100 000 in month')
# plt.plot(data_sale.year, data_sale.clients300, linewidth=5, label=f' >= 300 000 in month')
# plt.plot(data_sale.year, data_sale.clients500, linewidth=5, label=f' >= 500 000 in month')

# ax.legend()
# fig.set_figwidth(12)
# fig.set_figheight(12)
print(data_sale)
plt.grid()
plt.show()
