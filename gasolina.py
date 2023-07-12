grafico = sns.lineplot(data=tabela,x="dia",y="venda"
grafico = sns.lineplot(data=tabela,x="dia",y="venda"
grafico.set(title="Vendas de Gasolina por dia",xlabel="Dia",ylabel="Vendas"
grafico.get_figure().savefig("gasolina.png")