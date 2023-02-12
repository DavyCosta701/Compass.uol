with total_vendas as (
	SELECT t1.cdvdd, t1.nmvdd, t2.qtd*t2.vrunt as valor_total, t1.perccomissao
	from tbvendedor as t1
	left join tbvendas as t2
	on t1.cdvdd = t2.cdvdd
	and t2.status = 'Concluído'

), 
soma_total as (
	SELECT cdvdd, nmvdd, sum(valor_total) as valor_total_vendas,perccomissao
	from total_vendas
	GROUP by nmvdd
)
SELECT nmvdd as vendedor, valor_total_vendas, round(valor_total_vendas * (perccomissao/100.0), 2) as comissao from soma_total
group by vendedor
order by comissao desc
