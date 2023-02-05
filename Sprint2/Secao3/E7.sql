with tabela1 as (

	select t1.nome, t1.codautor, t2.titulo
	from autor as t1 left join livro as t2
	on t1.codautor = t2.autor
	
)
select nome from tabela1 where titulo is NULL
order by nome;
	