import multiprocessing
from clickhouse_driver import Client


def execute_query(query):
    client = Client(
        host='g2.plzvpn.ru',
        user='default',
        password='1',
        port='9000',
        database='test',
        # settings={'use_numpy': True}
    )
    result = client.execute(query)
    for row in result:
        print(row)


if __name__ == '__main__':
    queries = [
        'SELECT * FROM Prodazhi LIMIT 6',
        'SELECT * FROM Goroda LIMIT 4',
    ]
    pool = multiprocessing.Pool(processes=len(queries))
    pool.map(execute_query, queries)
    pool.close()
    pool.join()
