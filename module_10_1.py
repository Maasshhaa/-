import threading
import time
from turtledemo.penrose import start


def write_words(word_count, file_name):
    file = open('file_name', 'a', encoding='utf-8')
    for i in range(word_count):
        time.sleep(0.1)
        file.write(f'Какое-то слово №{i} \n')
    file.close()
    return print(f'Завершилась запись в файл {file_name}')

stared_at = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
ended_at = time.time()
elapsed = ended_at - stared_at
print(f'Работа потоков {round(elapsed,2)}')


stared_at = time.time()
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread1.start()
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread2.start()
thread3  = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread3.start()
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread4.start()
thread3.join()
ended_at = time.time()
elapsed = ended_at - stared_at
print(f'Работа потоков {round(elapsed,2)}')