import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 20)  # расширение области видимости данных таблицы
pd.set_option('display.width', 2000)

clients_list = ['Щемерко', 'СОНАР']
len_list = len(clients_list)
num = 0


def clients(client, len_list, num):
    Client_data = pd.read_excel(f'{client}.xls')  # , converters={"Дата": pd.to_datetime})
    Client_data = Client_data[['Дата', "Сумма"]]
    Client_data.columns = ['date', 'sum_ship']
    for i in range(len(Client_data)):
        string = Client_data.date[i][6:10] + Client_data.date[i][2:5]
        Client_data.iloc[[i], [0]] = string
    Client_data = Client_data.groupby('date', as_index=False).agg({'sum_ship': 'sum'})

    # fig, ax = plt.subplots()  # подготовка графиков
    # ax.set(title='trading')  # наименование графика
    #
    # #  Добавляем подписи к осям:
    # ax.set_xlabel('месяц')
    # ax.set_ylabel('суммы док-в продаж, шт')

    plt.subplot(len_list, 1, num)
    plt.plot(Client_data['date'], Client_data.sum_ship)
    plt.grid()
    print(f'{client}: ', Client_data)
    print(f'{client}: summ ', Client_data.sum_ship.sum())


for client in clients_list:
    num += 1
    clients(client, len_list, num)
    plt.tick_params(labelrotation=25)

plt.show()



