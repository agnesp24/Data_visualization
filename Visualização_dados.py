import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('clientes-v3-preparado.csv')
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
print(df.head(20).to_string())

def hist():

    #Histograma
    # plt.hist(df['salario'])
    # plt.show()

    #Histograma - parâmetros
    plt.figure(figsize=(10, 6))
    plt.hist(df['salario'], bins=100, color='blue', alpha=0.8)
    plt.title('Histograma - Distribuição de Salários')
    plt.xlabel('Salário')
    plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))
    plt.ylabel('Frequência')
    plt.grid(True)
    plt.show()

def disp():

    #Dispersão
    plt.scatter(df['salario'], df['salario'])
    plt.title('Dispersão: Salário e Salário')
    plt.xlabel('Salário')
    plt.ylabel('Salário')
    plt.show()

def multiplos_graf():

    #Múltiplos gráficos

    plt.figure(figsize=(10, 6))
    plt.subplot(2, 2, 1)  # 2 linhas - 2 colunas - 1° gráfico
    #Gráfico de dispersão
    plt.scatter(df['salario'], df['salario'])
    plt.title('Dispersão: Salário e Salário')
    plt.xlabel('Salário')
    plt.ylabel('Salário')

    plt.subplot(1, 2, 2) #1 Linha, 2 colunas, 2º gráfico
    #Gráfico de dispersão
    plt.scatter(df['salario'], df['anos_experiencia'], color='#5883a8', alpha=0.6, s=30)
    plt.title('Dispersão: Idade e Anos Experiência')
    plt.xlabel('Salário')
    plt.ylabel('Anos de experiência')

    #Mapa de calor
    correlacao = df[['salario', 'anos_experiencia']].corr()
    plt.subplot(2, 2, 3)
    sns.heatmap(correlacao, annot=True, cmap='coolwarm')
    plt.title('Mapa de Calor: Correlação Salário e Idade')

    plt.tight_layout()
    plt.show()

def matplot():

    #Gráfico de barras
    # plt.figure(figsize=(10,6))
    # df['nivel_educacao'].value_counts().plot(kind='bar', color='#90ee70') #Função do PANDAS para criar gráfico
    # plt.title('Gráfico de Barras: Divisão de Escolaridade')
    # plt.xlabel('Nível de Educação')
    # plt.ylabel('Quantidade')
    # plt.xticks(rotation=0)
    # plt.show()

    #Outra forma de fazer gráficos de barra
    x = df['nivel_educacao'].value_counts().index
    y = df['nivel_educacao'].value_counts().values

    # plt.figure(figsize=(10,6))
    # plt.bar(x, y, color='#60aa65')
    # plt.title('Gráfico de Barras: Divisão de Escolaridade V2')
    # plt.xlabel('Nível de Educação')
    # plt.ylabel('Quantidade')
    # plt.xticks(rotation=0)
    # plt.show()

    #Gráfico de Pizza
    # plt.figure(figsize=(10,6))
    # plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
    # plt.title('Gráfico de Pizza: Nível de Educação')
    # plt.show()

    #Gráfico de dispersão
    plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Reds')
    plt.colorbar(label='Contagem')
    plt.xlabel('Idade')
    plt.ylabel('Salário')
    plt.title('Gráfico de Dispersão: Idade e Salário')
    plt.show()

def sea():

    #Gráfico de Dispersão
    # sns.jointplot(x='idade', y='salario', data=df, kind='scatter') #Scatter, Hist, Hex, KDE, Reg, Resid.
    # plt.show()

    #Gráfico de Densidade
    # plt.figure(figsize=(10,6))
    # sns.kdeplot(df['salario'], fill=True, color='#863e9c')
    # plt.title('Gráfico de Densidade: Salários')
    # plt.ylabel('Densidade')
    # plt.xlabel('Salário')
    # plt.show()

    #Gráfico de Pairplot - Dispersão e Histograma
    # sns.pairplot(df[['idade', 'salario', 'anos_experiencia']])
    # plt.show()

    #Gráfico de Regressão
    # sns.regplot(x='idade', y='salario', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
    # plt.title('Gráfico de Regressão: Salário por Idade')
    # plt.xlabel('Idade')
    # plt.ylabel('Salário')
    # plt.show()

    #Gráfico Countplot com HUE (agrupamento)
    sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
    plt.legend(title='Nível de Educação')
    plt.xlabel('Estado Civil')
    plt.show()

def atividade():
    df_correlacao = df[['salario', 'idade', 'anos_experiencia', 'numero_filhos',
                        'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod']].corr()
    #Heatmap de correlação
    plt.figure(figsize=(10,8))
    sns.heatmap(df_correlacao, annot=True, fmt='.2f')
    plt.title('Mapa de Calor: Correlação entre Variáveis')
    plt.show()

    #Countplot
    sns.countplot(x='estado_civil', data=df)
    plt.title('Gráfico Estado Civil')
    plt.xlabel('Estado Civil')
    plt.show()

    

#hist()
#disp()
#multiplos_graf()
#matplot()
#sea()
atividade()