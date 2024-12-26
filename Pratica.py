from enum import nonmember

import pandas as pd
import seaborn
import matplotlib.pyplot as plt

def treatment():
    df = pd.read_csv('ecommerce_preparados.csv')
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    #Dropping null entries
    df = df.dropna()

    #Displaying the number of null, duplicated and unique entries
    # print('Null: ', df.isnull().sum().sum())
    # print('Duplicates: ', df.duplicated().sum().sum())
    # print('Unique: ', df.nunique())
    df['Temporada'] = df['Temporada'].str.strip()

    #Renaming category inside Gênero for a better graph view
    df['Gênero'] = df['Gênero'].replace('roupa para gordinha pluss P ao 52', 'Plus Size')

    #Normalizing the data fields
    df['Marca'] = df['Marca'].str.title()
    df['Material'] = df['Material'].str.capitalize()
    df['Temporada'] = df['Temporada'].str.title()

    #Creating a cordinal codefication for 'Gênero'
    genero = {'Masculino': 1, 'Feminino': 2, 'Meninas': 3, 'Meninos': 4, 'Sem gênero': 5, 'Plus Size': 6,
              'Sem gênero infantil': 7, 'Unissex': 8, 'Bebês': 9}
    df['Gênero_Cod'] = df['Gênero'].map(genero)

    # #Creating a frequency code for Gênero
    # Gênero_Freq = df['Gênero'].value_counts() / len(df)
    # df['Gênero_Freq'] = df['Gênero'].map(Gênero_Freq)

    #Saving the dataframe using only the columns we'll use
    # df = df[['Nota', 'N_Avaliações', 'Desconto', 'Marca', 'Marca_Cod', 'Material', 'Material_Cod',
    #          'Gênero', 'Gênero_Cod', 'Temporada', 'Temporada_Cod', 'Qtd_Vendidos_Cod',
    #         'Preço', 'Nota_MinMax', 'N_Avaliações_MinMax', 'Desconto_MinMax', 'Preço_MinMax',
    #         'Marca_Freq', 'Material_Freq']]

    df = df['Temporada']

    print(df.head(30))

    # print(df.tail(30))
    df.to_csv('ecommerce_preparados_v2.csv')

def graphs():

    df = pd.read_csv('ecommerce_preparados_v2.csv')
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    #Histogram graph - Preço
    # plt.figure(figsize=(10, 6))
    # plt.subplot(2, 2, 1)
    # plt.hist(df['Preço'], color='blue', bins=100, alpha=0.8)
    # plt.xticks(ticks=range(0, int(df['Preço'].max())+25, 25))
    # plt.title('Histograma - Preço')
    # plt.xlabel('Preços')
    # plt.ylabel('Frequência')
    # plt.grid(True)

    #Dispersion graph -

    #Pizza graph - Marca
    # y = df['Temporada'].value_counts().values
    # x = df['Temporada'].value_counts().index
    # plt.figure(figsize=(10,6))
    # plt.pie(y, labels=None, startangle=30, autopct='%d%%')
    # plt.title('Frequência de Gêneros')
    # plt.tight_layout()
    # plt.legend(title='Gêneros', labels=x)
    # plt.show()

    #Heat map

    #Bar graph
    # plt.figure(figsize=(12,6))
    # df['Gênero'].value_counts().plot(kind='bar', color='#90ee70')
    # plt.title('Frequência - Gênero')
    # plt.xlabel('Gênero')
    # plt.xticks(rotation=0)
    # plt.ylabel('Frequência')
    # plt.tight_layout()
    # plt.show()

    #Density graph

    #Rgression graph

treatment()
#graphs()