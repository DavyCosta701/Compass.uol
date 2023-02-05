select t1.nome, t1.codautor, t1.nascimento, count(t2.titulo) as quant_livros
from autor as t1 left join livro as t2
on t1.codautor = t2.autor
GROUP by autor
order by nome;

