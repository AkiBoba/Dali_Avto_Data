import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 20)  # расширение области видимости данных таблицы
pd.set_option('display.width', 2000)

date_list = [2015, 2016, 2017, 2018, 2019]
data_sale = pd.DataFrame()
for year in date_list:
    df2015 = pd.read_excel(f'{year}.xls')

    df2015 = df2015.iloc[11:, [0, 16, 20, 22, 24, 25, 26, 27, 28]]

    df2015.columns = ['docs', 'price_ship', 'sum_ship', 'prof_ship', 'ship_per', 'price_pay', 'sum_pay', 'prof_pay',
                      'pay_per']
    # print(df2015.head(30))
    df2015 = df2015[df2015.docs.str.contains('Реализация') == True]
    df2015.index = [n for n in range(len(df2015))]
    for i in range(len(df2015)):
        string = df2015.docs[i][48:52]  # + df2015.docs[i][44:47]
        df2015.docs[i] = string

    df2015 = df2015[['docs', 'sum_ship']]
    data_sale = data_sale.append(df2015)
data_sale = data_sale.groupby('docs', as_index=False).agg({'sum_ship': 'sum'})
# data_ship = data_sale.groupby('docs', as_index=False).agg({'sum_ship': 'count'})
# print(data_sale.head())

fig, ax = plt.subplots()  # подготовка графиков
ax.set(title='trading')  # наименование графика

#  Добавляем подписи к осям:
ax.set_xlabel('year')
ax.set_ylabel('Суммы отгрузок,100*млн., руб., шт')

ax.tick_params(labelrotation=45)
plt.plot(data_sale.docs, data_sale['sum_ship'], label=f'2015-2019 year')
# plt.plot(data_ship.docs, data_ship['sum_ship'])
ax.legend()
# fig.set_figwidth(12)
# fig.set_figheight(12)
plt.show()
