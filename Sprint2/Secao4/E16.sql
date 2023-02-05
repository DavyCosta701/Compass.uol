with list_estado as (
	select estado, nmpro, qtd
	from tbvendas
	where status = 'Concluído'
)

select estado, nmpro, round(avg(qtd),4) from list_estado
GROUP by estado, nmpro
order by estado