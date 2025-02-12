#Thread 2
#Processamento de imagem
import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

t1 = time.perf_counter()

size = (1200, 1200)

'''
A seguir, irá ser definido uma função que utiliza o nome da imagem como parâmetro, abrindo a imagem repassada,
aplicando um filtro na imagem, sendo esse filtro um efeito de desfoque, e redefiniindo também o tamanho da imagem, utili-
zando o parametro size, definido na linha 28, e por fim, salvando no diretório "Processed"
'''


def process_image(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'processado/{img_name}')
    print(f'{img_name} foi processada!')



'''  
Abaixo temos a função ProcessPool, que tem por finalidadeexecutar e gerenciar os processos, sendo que utilizando a 
funcao definida na linha 37, será repassada o parametro process_image e seus respectivos nomes. 
Desse modo, a função é executada individualmente com os itens da lista, sendo executadas em paralelo. 
'''

with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names)


t2 = time.perf_counter()

print(f'Completado em {t2-t1} segundos')
