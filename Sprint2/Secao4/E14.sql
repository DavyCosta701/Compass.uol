with lista_venda as (
	select estado, vrunt * qtd as bruto
	from tbvendas

)
SELECT estado, round(avg(bruto),2) as gastomedio  from lista_venda
GROUP by estado
order by gastomedio desc;