with lista_prod as (
	select cdpro, nmcanalvendas, nmpro, qtd
	from tbvendas
	where status = 'Concluído'
	

)
SELECT cdpro, nmcanalvendas, nmpro, sum(qtd) as quantidade_vendas from lista_prod
GROUP by nmcanalvendas, nmpro
order by quantidade_vendas