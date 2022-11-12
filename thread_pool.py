import time
import threading
from concurrent.futures import ThreadPoolExecutor


def test_function_thread_pool(item):
    print(f'Start thread id ({threading.get_ident()}) data = {item["name"]}')
    time.sleep(2)
    print(f'Finished thread id = {threading.get_ident()}')


if __name__ == '__main__':
    workers = 5
    data_list = [
        {'name': 'a'},
        {'name': 'b'},
        {'name': 'c'},
        {'name': 'd'},
        {'name': 'e'}
    ]

    print('Start Processing')
    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(test_function_thread_pool, data_list)
    print('Process End.')
