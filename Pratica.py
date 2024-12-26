from enum import nonmember

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def treatment():
    df = pd.read_csv('ecommerce_preparados.csv')
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    #Normalizing the data fields
    df['Marca'] = df['Marca'].str.title()
    df['Material'] = df['Material'].str.capitalize()
    df['Temporada'] = df['Temporada'].str.title()

    #Dropping null entries
    df = df.dropna()

    #Displaying the number of null, duplicated and unique entries
    # print('Null: ', df.isnull().sum().sum())
    # print('Duplicates: ', df.duplicated().sum().sum())
    # print('Unique: ', df.nunique())

    #Renaming categories in Temporada
    df['Temporada'] = df['Temporada'].str.strip()
    df['Temporada'] =  df['Temporada'].replace('Primavera-Verão Outono-Inverno', 'Primavera/Verão/Outono/Inverno')
    df['Temporada'] =  df['Temporada'].replace('Primavera-Verão - Outono-Inverno', 'Primavera/Verão/Outono/Inverno')
    df['Temporada'] =  df['Temporada'].replace('Não Definido', 'Outro')

    #Renaming category in Gênero
    df['Gênero'] = df['Gênero'].replace('roupa para gordinha pluss P ao 52', 'Plus Size')

    #Creating a cordinal codefication for 'Gênero'
    genero = {'Masculino': 1, 'Feminino': 2, 'Meninas': 3, 'Meninos': 4, 'Sem gênero': 5, 'Plus Size': 6,
              'Sem gênero infantil': 7, 'Unissex': 8, 'Bebês': 9}
    df['Gênero_Cod'] = df['Gênero'].map(genero)

    #Saving the dataframe using only the columns we'll use
    df = df[['N_Avaliações', 'Desconto', 'Marca', 'Marca_Cod', 'Material', 'Material_Cod',
             'Gênero', 'Gênero_Cod', 'Temporada', 'Temporada_Cod', 'Qtd_Vendidos_Cod',
            'Preço', 'Marca_Freq', 'Material_Freq']]

    print(df.head(10))

    # print(df.tail(30))
    df.to_csv('ecommerce_preparados_v2.csv')

def graphs():

    df = pd.read_csv('ecommerce_preparados_v2.csv')
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    #Histogram graph - Preço
    plt.figure(figsize=(14, 8))
    plt.subplot(2, 2, 1) #2 Linhas, 2 Colunas, 1º Gráfico
    plt.hist(df['Preço'], color='blue', bins=100, alpha=0.8)
    plt.xticks(ticks=range(0, int(df['Preço'].max())+25, 25))
    plt.title('Histograma - Preço')
    plt.xlabel('Preços')
    plt.ylabel('Frequência')
    plt.grid(True)

    #Heat map
    plt.subplot(1, 2, 2) #1 Linha, 2 Colunas, 2° Gráfico
    corr = df[['Preço', 'Desconto']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Mapa de Calor - Preço e Desconto')

    #Density graph
    plt.subplot(2, 2, 3)
    sns.kdeplot(df['Preço'], fill=True, color='#90ee70')
    plt.title('Gráfico de Densidade - Preços')
    plt.xlabel('Preços')
    plt.ylabel('Densidade')

    plt.tight_layout()
    plt.show()

    #Dispersion graph - Preço e N_Avaliações
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.hexbin(df['Preço'], df['N_Avaliações'], cmap='Reds', gridsize=40)
    plt.colorbar(label='Contagem')
    plt.ylabel('Número de Avaliações')
    plt.xlabel('Preço')

    #Regression graph
    plt.subplot(1, 2, 2)
    sns.regplot(x='Preço', y='Qtd_Vendidos_Cod', data=df, color='#90ee70',
                scatter_kws={'alpha': 0.5, 'color': '#34c289'})
    plt.title('Gráfico de Regressão - Quantidade de Vendas por Preço')
    plt.xlabel('Preço')
    plt.ylabel('Quantidade Vendidos')
    plt.tight_layout()
    plt.show()

    #Bar graph - Gênero
    plt.figure(figsize=(12, 6))
    df['Gênero'].value_counts().plot(kind='bar', color='#90ee70')
    plt.title('Frequência - Gênero')
    plt.xlabel('Gênero')
    plt.xticks(rotation=0)
    plt.ylabel('Frequência')
    plt.tight_layout()
    plt.show()

    #Pizza graph - Temporada
    y = df['Temporada'].value_counts().values
    x = df['Temporada'].value_counts().index
    plt.figure(figsize=(10,6))
    plt.pie(y, labels=x, startangle=30, autopct='%d%%')
    plt.title('Frequência - Temporada')
    plt.tight_layout()
    plt.show()

treatment()
graphs()