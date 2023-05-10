import random
import names


if __name__ == "__main__":
    random.seed(40)
    aux =  [names.get_full_name() for _ in range(3000)]
    with open('nomes_aleatorios.txt', 'w') as n:
         n.write('\n'.join([random.choice(aux) for _ in range(10000000)]))
        
    