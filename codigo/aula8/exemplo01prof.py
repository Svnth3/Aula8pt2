# Plotando Gráfico de Barras
# Barras e Colunas (barh e bar)
try:
    # Cria uma figura com 1 linha e 2 colunas de subgráficos (side by side)
    # figsize define o tamanho da figura total
    fig, ax = plt.subplots(1, 2, figsize=(18, 6))
    

    # OUTLIERS INFERIORES
    # Verifica se existem outliers inferiores
    if not df_roubo_veiculo_outliers_inferiores.empty:
        # Ordena os dados de forma crescente pelo número de roubos
        dados_inferiores = df_roubo_veiculo_outliers_inferiores.sort_values(by='roubo_veiculo', ascending=True)
        
        # Cria gráfico de barras horizontais com os municípios e seus valores
        ax[0].barh(dados_inferiores['munic'], dados_inferiores['roubo_veiculo'])
    
    else:
        # Caso não haja outliers inferiores, exibe os 10 municípios que obtiveram menos roubos (bootom 10)
        dados_inferiores = df_roubo_veiculo_menores.sort_values(by='roubo_veiculo', ascending=True).head(10)

        # ax[0].text(0.5, 0.5, 'Sem Outliers Inferiores', ha='center', va='center', fontsize=12)
        barras = ax[0].bar(dados_inferiores['munic'], dados_inferiores['roubo_veiculo'], color='black')
        ax[0].bar_label(barras, label_type='edge', padding=3, fontsize=8)
        ax[0].tick_params(axis='x', rotation=75, labelsize=8)
        # Define o título do subplot
        ax[0].set_title('Menores Roubos')
        # Remove os marcadores dos eixos x e y
        ax[0].set_xticks([])
        ax[0].set_yticks([])

        # ##### VISUAL ######
        # Rótulo no final das barras e com tam 8
        # barras = ax[0].bar(dados_inferiores['munic'], dados_inferiores['roubo_veiculo'], color='green')
        # ax[0].bar_label(barras, label_type='edge', padding=3, fontsize=8)
        # # rotaciona o eixo x para melhorar a visualização
        # ax[0].tick_params(axis='x', rotation=75, labelsize=8)
 
    # OUTLIERS SUPERIORES
    # Verifica se existem outliers superiores
    if not df_roubo_veiculo_outliers_superiores.empty:
        # Ordena os dados de forma crescente
        dados_superiores = df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo', ascending=True)

        # Cria o gráfico de barras horizontais com os municípios e seus valores
        ax[1].barh(dados_superiores['munic'], dados_superiores['roubo_veiculo'], color='black')
        # Define o título e o rótulo do eixo x
        ax[1].set_title('Outliers Superiores')
        ax[1].set_xlabel('Total Roubos de Veículos')

        # ###### "VISUAL" #####
        # Rótulo de dados 0 casas decimais, edge "final da barra", tamanho 8 a 1 padding "distância"
        barras = ax[1].barh(dados_superiores['munic'], dados_superiores['roubo_veiculo'], color='black')
        ax[1].bar_label(barras, fmt='%.0f', label_type='edge', fontsize=8, padding=1)  
        # Tamanho do conteúdo do eixo Vertical "Y"
        ax[1].tick_params(axis='y', labelsize=8)

    else:
        # Caso não haja outliers superiores, exibe uma mensagem centralizada
        ax[1].text(0.5, 0.5, 'Sem outliers superiores', ha='center', va='center', fontsize=12)

        # Define o título do subplot
        ax[1].set_title('Outliers Superiores')

        # Remove os marcadores dos eixos x e y
        ax[1].set_xticks([])
        ax[1].set_yticks([])

    # Ajusta automaticamente os elementos do layout para não se sobreporem
    plt.tight_layout()

    # Exibe os gráficos
    plt.show()

except Exception as e:
    print(f'Erro ao plotar {e}')