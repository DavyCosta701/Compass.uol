with lista_editora as (
	select t1.nome, t1.endereco, count(*) as quantidade
	from editora as t1 left join livro as t2
	on t1.codeditora = t2.editora
	GROUP by t1.nome
	order by quantidade
)
select t3.quantidade, t3.nome, t4.estado, t4.cidade
from lista_editora as t3 left join endereco as t4
on t3.endereco = t4.codendereco
order by quantidade desc
limit 5;