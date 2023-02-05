select t1.nome
	from autor as t1
	left join livro as t2
	on t1.codautor = t2.autor
		left join editora as t3
		on t2.editora = t3.codeditora
			inner join endereco as t4
			on t3.endereco = t4.codendereco
			and t4.estado NOT in ('PARANÁ')
	order by t1.nome;