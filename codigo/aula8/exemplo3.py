import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


try: 
    print('Obtendo dados...')
    Endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    df_ocorrencia = pd.read_csv(Endereco_dados, sep=";", encoding='iso-8859-1')
    # print(df_ocorrencia.head())

    df_ocorrencia = df_ocorrencia[['munic', 'roubo_veiculo']]

    df_roubo_veiculo = df_ocorrencia.groupby('munic').sum('roubo_veiculo').reset_index()
    # print(df_roubo_veiculo.to_string())


except Exception as e:
    print(f'Erro: {e}')
    exit()
try:
    print("Obtendo informações sobre padrão de roubos de veiculos...")
    array_roubo_carros = np.array(df_roubo_veiculo['roubo_veiculo'])

    mediana = np.median(array_roubo_carros)
    media = np.mean(array_roubo_carros)
    distancia = abs((media - mediana) / mediana)
    # print('media:', media)
    # print('mediana:', mediana)
    # print(f'Distancia: {distancia:.3f}')

    q1 = np.quantile(array_roubo_carros, 0.25, method='weibull')
    q2 = np.quantile(array_roubo_carros, 0.50, method='weibull')
    q3 = np.quantile(array_roubo_carros, 0.75, method='weibull')


    # Medidas de dispersão
    print('/nMedidas de Dispersão')
    
    maximo = np.max(array_roubo_carros)
    minimo = np.min(array_roubo_carros)
    amplitude_total = maximo - minimo
    

    df_roubo_veículo_menores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < q1]
    df_roubo_veículo_maiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > q3]
    # print(df_roubo_veículo_menores.sort_values(by='roubo_veiculo', ascending=True))
    # print("")
    # print(100*"-")
    # print("")
    # print(df_roubo_veículo_maiores.sort_values(by='roubo_veiculo', ascending=False ))

    iqr = q3 - q1 
    limite_superior = q3 + (1.5*iqr)
    limite_inferior = q1 - (1.5*iqr)
    

    print('\nLimites - Medidasde posição')
    print(f'Limite Inferior: {limite_inferior}')
    print(f'Minimo: {minimo}')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')
    print(f'IQR: {iqr}')
    print(f'Máximo: {maximo}')
    print(f'Limite Superior: {limite_superior}')
    print(f'Media: {media:.2f}')
    print(f'Mediana: {mediana:.2f}')
    print(F'distância media e mediana: {distancia}')

    df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior]
    df_roubo_veiculo_outliers_inferior = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior]
    
    print("\nlimite inferior")
    if len(df_roubo_veiculo_outliers_inferior) == 0:
        print("Não tem outliers inferiores")
    else:
        print(df_roubo_veiculo_outliers_inferior.sort_values(by='roubo_veiculo', ascending=True))

    
    print("\nlimite Superior")
    if len(df_roubo_veiculo_outliers_superiores) == 0:
        print("Não tem outliers superiores")
    else:
        print(df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=False))



except Exception as a:
    print(f'Erro {a}')

#pip install matplotlib
try:
    plt.subplots(2,2, figsize=(18, 6))
    
    plt.subplot(2,2,1)
    
    plt.boxplot(array_roubo_carros, vert=False, showmeans=True)

    # plt.boxplot(array_roubo_carros, vert=False, showmeans=True)


    
    plt.tight_layout()
    plt.show()
except Exception as z:
    print(f'erro: {z}')
    exit
