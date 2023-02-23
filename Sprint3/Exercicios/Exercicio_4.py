def primo(x):
    for i in range (2, x):
        if x%i==0:
            return None
    return print(x)



for i in range (2,100):
    primo(i)
    