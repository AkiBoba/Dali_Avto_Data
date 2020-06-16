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
         # 'clients': clients,
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
    df2015 = df2015[['docs', 'price_ship', 'sum_ship', 'prof_ship', 'ship_per']]
    df2015 = df2015[df2015.docs.str.contains('Реализация') != True]
    clients.append(df2015.ship_per[df2015.docs.str.contains('Итого') == True])
    df2015 = df2015[df2015.docs.str.contains('Итого') != True]  #
    df2015 = df2015.fillna(0)
    df2015 = df2015[df2015.sum_ship != 0]
    # print(f'{year}', df2015.docs.count())

    clients0.append((df2015.prof_ship[df2015.sum_ship < 30000 * 12].sum() / df2015.price_ship[
        df2015.sum_ship < 30000 * 12].sum()) * 100)
    clients30.append(
        (df2015.prof_ship[(df2015.sum_ship < 50000 * 12) & (df2015.sum_ship >= 30000 * 12)].sum() / df2015.price_ship[
            (df2015.sum_ship < 50000 * 12) & (df2015.sum_ship >= 30000 * 12)].sum()) * 100)
    clients50.append(
        (df2015.prof_ship[(df2015.sum_ship < 100000 * 12) & (df2015.sum_ship >= 50000 * 12)].sum() / df2015.price_ship[
            (df2015.sum_ship < 100000 * 12) & (df2015.sum_ship >= 50000 * 12)].sum()) * 100)
    clients100.append(
        (df2015.prof_ship[(df2015.sum_ship < 300000 * 12) & (df2015.sum_ship >= 100000 * 12)].sum() / df2015.price_ship[
            (df2015.sum_ship < 300000 * 12) & (df2015.sum_ship >= 100000 * 12)].sum()) * 100)
    clients300.append(
        (df2015.prof_ship[(df2015.sum_ship < 500000 * 12) & (df2015.sum_ship >= 300000 * 12)].sum() / df2015.price_ship[
            (df2015.sum_ship < 500000 * 12) & (df2015.sum_ship >= 300000 * 12)].sum()) * 100)
    clients500.append((df2015.prof_ship[df2015.sum_ship >= 500000 * 12].sum() / df2015.price_ship[
        df2015.sum_ship >= 500000 * 12].sum()) * 100)

    # clients0.append(df2015.docs.count())
    # print(sales['clients0']+sales['clients30']+sales['clients50']+sales['clients100']+sales['clients300']+sales['clients500'])
data_sale = pd.DataFrame(sales)

# print(data_sale)
fig, ax = plt.subplots()  # подготовка графиков
ax.set(title='trading')  # наименование графика

#  Добавляем подписи к осям:
ax.set_xlabel('year')
ax.set_ylabel('Процент наценки по отгрузке, %')

ax.tick_params(labelrotation=45)
# plt.bar(data_sale.year + .1, data_sale.clients, width=.1, label=f'clients all')
plt.subplot(611)
plt.plot(data_sale.year, data_sale.clients0, color='b', label=f' сумма отгрузок < 30 тр в мес')
plt.grid()
plt.legend()
plt.subplot(612)
plt.plot(data_sale.year, data_sale.clients30, color='r', label=f' 50 > сумма отгрузок >= 30 тр в мес')
plt.grid()
plt.legend()
plt.subplot(613)
plt.plot(data_sale.year, data_sale.clients50, color='c', label=f' 100 > сумма отгрузок >= 50 тр в мес')
plt.grid()
plt.legend()
plt.subplot(614)
plt.plot(data_sale.year, data_sale.clients100, color='y', label=f' 300 > сумма отгрузок >= 100 тр в мес')
plt.grid()
plt.legend()
plt.subplot(615)
plt.plot(data_sale.year, data_sale.clients300, color='k', label=f' 500 > сумма отгрузок >= 300 тр в мес')
plt.grid()
plt.legend()
plt.subplot(616)
plt.plot(data_sale.year, data_sale.clients500, color='g', label=f' сумма отгрузок >= 500 тр в мес')
plt.grid()
plt.legend()
# ax.text(2017, 500, 'всего клиентов')
#
# ax.text(2017, 300, 'клиенты от 30 тр')

ax.legend()
fig.set_figwidth(12)
fig.set_figheight(12)
print(data_sale)
ax.grid()
plt.show()
