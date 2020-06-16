import pandas as pd
import matplotlib.pyplot as plt

doc_list = ['2015реализации', '2016реализации', '2017реализации', '2018реализации', '2019реализации']


def sales_years(docs):
    df = pd.read_excel(f'D:\PycharmProjects\Dali_Avto_Data\\{docs}.xlsx')

    df = df.iloc[0:, [1, 3, 7, 11, 19, 21, 29, 35, 39]]

    df.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    df.fillna(0)

    numbers = []
    codes = []
    products = []
    weights = []
    counts = []
    prices = []
    summ = []

    numbers = list(df['1'][df['2'] == 'ДАЛИ-авто'])
    products = list(df['6'][df['2'] == 'ДАЛИ-авто'])
    codes = list(df['3'][df['2'] == 'ДАЛИ-авто'])
    weights = list(df['5'][df['2'] == 'ДАЛИ-авто'])
    counts = list(df['7'][df['2'] == 'ДАЛИ-авто'])
    prices = list(df['8'][df['2'] == 'ДАЛИ-авто'])
    summ = list(df['9'][df['2'] == 'ДАЛИ-авто'])

    sales = {
        'numbers': numbers,
        'codes': codes,
        'products': products,
        'weights': weights,
        'counts': counts,
        'prices': prices,
        'summ': summ
    }

    sale = pd.DataFrame(sales)

    sale.head()

    df1 = pd.read_excel('D:\PycharmProjects\Dali_Avto_Data\\Поступление_шланги.xls')

    df1 = df1.iloc[0:, [3, 7, 13, 37]]

    df1.columns = ['1', '2', '3', '4']

    liquid = list(df1['2'][df1['1'] == 'ДАЛИ-авто'])

    zacup = sale[sale.codes.isin(liquid) == True]

    prod_sale = zacup.groupby(['codes', 'products'], as_index=False).agg(
        {'weights': 'sum', 'counts': 'sum', 'summ': 'sum'})

    prod_sale.sort_values(by='counts')

    # prod_sale.plot(kind='bar', x='codes', y='counts',  label=f'sale of products')
    #
    # plt.show()

    return prod_sale.summ.sum()



years = [2015, 2016, 2017, 2018, 2019]
sum_sale = []
for docs in doc_list:
    sum_sale.append(sales_years(docs))

years_sale = pd.DataFrame({'years': years, 'sum_sale': sum_sale})

years_sale.plot(kind='bar', x='years', y='sum_sale', label=f'sale of products')
print(years_sale)
plt.show()