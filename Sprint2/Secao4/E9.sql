with list_prod as (
	select count(*) as vendas,cdpro,nmpro from tbvendas where dtven BETWEEN '2014-02-03' and '2018-02-02'
	GROUP by cdpro
	ORDER by vendas desc
	limit 1

)
select cdpro, nmpro from list_prod;