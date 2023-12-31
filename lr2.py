import asyncio
from clickhouse_driver import Client


async def execute_query_async(query):
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


async def main():
    queries = [
        'SELECT * FROM Prodazhi LIMIT 4',
        'SELECT * FROM Goroda LIMIT 2',
    ]

    tasks = [execute_query_async(query) for query in queries]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
