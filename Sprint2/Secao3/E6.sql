with tabela1 as (
	select t1.codautor, t1.nome, t2.titulo
	from autor as t1 left join livro as t2
	on t1.codautor = t2.autor
)
select tabela1.nome, tabela1.codautor, count(tabela1.titulo) as total_livros from tabela1
GROUP by tabela1.codautor, tabela1.nome
order by total_livros desc
limit 1;