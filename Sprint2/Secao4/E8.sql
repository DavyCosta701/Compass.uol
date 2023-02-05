with status_concluido as (
	select cdvdd, count(status) as counter from tbvendas
	WHERE status = 'Concluído'
	group by cdvdd
	order by counter desc
	limit 1
	
)

select t1.cdvdd, t2.nmvdd
from status_concluido as t1
left join tbvendedor as t2
on t1.cdvdd = t2.cdvdd;
