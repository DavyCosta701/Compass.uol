def function(*args, **kwargs):
    for i in args:
        print(i)
    for k, v in kwargs.items():
        print(v)

function(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

