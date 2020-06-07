import pandas as pd
import matplotlib.pyplot as plt
import time

pd.set_option('display.max_columns', 20)  # расширение области видимости данных таблицы
pd.set_option('display.width', 2000)

Client_data = pd.read_excel(f'Щемерко продажи.xls')  # , converters={"Дата": pd.to_datetime})
Client_data = Client_data[['Дата', "Сумма"]]
Client_data.columns = ['date', 'sum_ship']
for i in range(len(Client_data)):
    string = Client_data.date[i][6:10] + Client_data.date[i][2:5]
    Client_data.date[i] = string
Client_data = Client_data.groupby('date', as_index=False).agg({'sum_ship': 'sum'})

print(Client_data)
#
fig, ax = plt.subplots()  # подготовка графиков
ax.set(title='trading')  # наименование графика

#  Добавляем подписи к осям:
ax.set_xlabel('месяц')
ax.set_ylabel('сумма продаж в месяц, руб.')

ax.tick_params(labelrotation=45)
plt.bar(Client_data.date, Client_data.sum_ship)

ax.legend()
fig.set_figwidth(12)
fig.set_figheight(12)
plt.show()