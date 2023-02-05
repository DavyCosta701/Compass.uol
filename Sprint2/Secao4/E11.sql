with lista_clientes as(
	select cdcli,nmcli, qtd*vrunt as valor_total
	from tbvendas
	where status = 'Concluído'

)
SELECT  cdcli, nmcli, sum(valor_total) as gasto from lista_clientes
GROUP by cdcli
ORDER by gasto DESC
LIMIT 1;