with vendedor_vendas as (
	select cdvdd, (qtd*vrunt) as valor

	from tbvendas
	where status = 'Concluído'
),
valor_final as (
	select cdvdd, sum(valor) as total_bruto
	from vendedor_vendas
	GROUP by cdvdd
	order by total_bruto
	limit 1
)
SELECT t1.cddep, t1.nmdep, t1.dtnasc, t2.total_bruto
from tbdependente as t1 inner JOIN valor_final as t2
on t1.cdvdd = t2.cdvdd;