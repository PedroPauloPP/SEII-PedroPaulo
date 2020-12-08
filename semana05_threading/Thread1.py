#Thread 1
 
 
import concurrent.futures
import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f'Suspender por {seconds} segundos')
    time.sleep(seconds)
    return f'Suspensão completa.{seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:

    f1 = executor.submit(do_something,1)  #Utiliza-se da função p/ esperar um resultado futuro
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, secs) for sec in secs]  #Responsável por enviar via parâmetro a função do_something especificando cada segundo e suas atribuições

    for f in concurrent.futures.as_completed(results):  #O laço printa os resultados das funções com resultados anteriormente futuros
       print(f.result())

    results = executor.map(do_something, secs)   #Entende quais são os parâmetros passados e repassa para o laço a seguir
    for result in results:
       print(result)
'''

threads = []

for _ in range(10):

    t = threading.Thread(target=do_something, args=[1.5]) #Aloca a função do_something como o target da thread a ser implementada
    t.start()           #Coloca inicio na thread implementada
    threads.append(t)   #Adiciona o ultimo termo no parametro threads[]

for t in threads:
    t.join()            #Agrupa todos os elementos indicados na Thread passada
'''
finish=time.perf_counter()
