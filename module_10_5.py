import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    file = open(name, 'r')
    while True:
        line = file.readline()
        all_data.append(line)
        if not line:
            break
    file.close()

filenames = [f'./file {number}.txt' for number in range(1, 5)]


# stared_at = time.time()
# result = list(map(read_info, filenames))
# ended_at = time.time()
# elapsed = ended_at - stared_at
# print(f'Время на выполнении функции последовательно - {elapsed}') #6.56002950668335

if __name__ == '__main__':
    stared_at = time.time()
    with Pool(processes=4) as pool:
        results = pool.map(read_info, filenames)
    ended_at = time.time()
    elapsed = ended_at - stared_at
    print(f'Время на выполнении функции многопроцессорно - {elapsed}') #2.6709513664245605

