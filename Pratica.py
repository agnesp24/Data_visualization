import pandas as pd
import seaborn
import matplotlib.pyplot as plt

def treatment():
    df = pd.read_csv('ecommerce_preparados.csv')
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    #Dropping null entries and displaying the number of null and duplicated entries.
    df = df.dropna()
    # print('Null: ', df.isnull().sum().sum())
    # print('Duplicates: ', df.duplicated().sum().sum())

    #Normalizing the data fields
    df['Marca'] = df['Marca'].str.title()
    df['Material'] = df['Material'].str.capitalize()
    df['Temporada'] = df['Temporada'].str.title()

    #Creating a cordinal codefication for 'Gênero'
    genero = {'Masculino': 1, 'Feminino': 2, 'Infantil': 3, 'Sem gênero': 4}
    df['Gênero_Cod'] = df['Gênero'].map(genero)

    #Saving the dataframe using only the columns we'll use
    df = df[['Nota', 'N_Avaliações', 'Desconto', 'Marca_Cod', 'Material_Cod', 'Gênero_Cod', 'Temporada_Cod', 'Qtd_Vendidos_Cod',
            'Preço', 'Nota_MinMax', 'N_Avaliações_MinMax', 'Desconto_MinMax', 'Preço_MinMax',
            'Marca_Freq', 'Material_Freq']]

    print(df.head(10))
    # print(df.tail(30))

    df.to_csv('ecommerce_preparados_v2.csv')
def graphs():

    df = pd.read_csv('ecommerce_preparados_v2.csv')
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    #Histogram graph - Preço
    plt.figure(figsize=(10, 6))
    plt.hist(df['Preço'], color='blue', bins=100, alpha=0.8)
    plt.xticks(ticks=range(0, int(df['Preço'].max())+25, 25))
    plt.title('Histograma - Preço')
    plt.xlabel('Preços')
    plt.ylabel('Frequência')
    plt.grid(True)
    plt.show()

#treatment()
graphs()