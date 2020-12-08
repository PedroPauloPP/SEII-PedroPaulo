#Thread 4
#Multi processamento

import concurrent.futures
import time
import multiprocessing


start = time.perf_counter()


def do_something(seconds):  #Ativa um "stand-by durante o tempo passado como parâmetro
    print(f'Stand-by em {seconds} segundo(s)...')
    time.sleep(seconds)
    return f'Completo em{seconds}'

p1 = multiprocessing.Process(target=do_something)  #Cria um objeto de multiprocessamento e coloca a função especificada na linha 12 como parâmetro a ser utilizado
p2 = multiprocessing.Process(target=do_something) 

p1.start()  #Inicia o processo da linha 17 e printa o tempo antes que ele acabe, já que o programa fica inativo 1 segundo
p2.start()

p1.join()  #Join garante que assim que o processo tiver sido completo, ele entra nos parâmetros abaixo do código
p2.join()


'''A seguir criaremos uma lista de processos. A cada vez que passa pelo laço é criado um processo
Para cada passo no laço utilizado, aloca-se o processo ao final da lista, visto que desse modo, garante-se que quando chegar
no ultimo paramentro dessa lista, a funcao implementada na linha 23, garante que o fim do processo foi atingido e que somente
assim, o script calcula o tempo total.
'''



processes = []
for _ in range(10):
    p = multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)

for process in processes:
    process.join()



'''
Na linha 53 foi utilizado o ProcessPoolExecutor. é padrão do python e pode ser usado para criar e gerenciar processos
É uma biblioteca padrao do python e gerenciamos processos com ela, sendo que podem ser feitos de forma unitaria, definindo
assim como a funcao irá processar cada coisa, sendo que o .map na linha 5 6especifica a funcao para cada segundo na lista
na mesma ordem em que foram iniciados.
'''

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    #results = [executor.submit(do_something, sec) for sec in secs]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Completo em {round(finish-start, 2)} segundos!')
