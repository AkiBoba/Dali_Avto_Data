import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 20)  # расширение области видимости данных таблицы
pd.set_option('display.width', 2000)

date_list = [2015, 2016, 2017, 2018, 2019]
data_sale = pd.DataFrame()
for year in date_list:
    df2015 = pd.read_excel(f'D:\PycharmProjects\Dali_Avto_Data\{year}.xls')

    df2015 = df2015.iloc[11:, [0, 16, 20, 22, 24, 25, 26, 27, 28]]

    df2015.columns = ['years', 'price_sale', 'sum_sale', 'profit', 'profit_per', 'price_pay', 'sum_pay', 'prof_pay',
                      'pay_per']
    df2015 = df2015[df2015.years.str.contains('Реализация') == True]
    df2015.index = [n for n in range(len(df2015))]
    for i in range(len(df2015)):
        string = df2015.years[i][48:52]
        df2015.years[i] = string

    df2015 = df2015[['years', 'sum_sale']]
    data_sale = data_sale.append(df2015)
data_sale = data_sale.groupby('years', as_index=False).agg({'sum_sale': 'sum'})
# data_ship = data_sale.groupby('years', as_index=False).agg({'sum_sale': 'count'})
print(data_sale)

fig, ax = plt.subplots()  # подготовка графиков
ax.set(title='trading')  # наименование графика

#  Добавляем подписи к осям:
ax.set_xlabel('year')
ax.set_ylabel('Суммы отгрузок,100*млн., руб., шт')

ax.tick_params(labelrotation=45)
# plt.subplot(311)
plt.plot(data_sale.years, data_sale.sum_sale, label=f'2015-2019 year')
# plt.plot(data_ship.docs, data_ship['sum_ship'])
ax.legend()
plt.grid()
# fig.set_figwidth(12)
# fig.set_figheight(12)
plt.show()
