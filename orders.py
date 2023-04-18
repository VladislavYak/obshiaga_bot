import psycopg2
from lib import PgConnect

class Order:
    customer_id: int
    courier_id: int
    message: str

class OrdersTable:
    def __init__(self, pg):
        self.pg = pg
    def create_order(self, customer_id, courier_id=None, message=None, is_finished=False):
        with self.pg.connection() as conn:
            with conn.cursor() as cur:
                sql_query = f"""
                INSERT INTO orders (customer_id, courier_id, message, is_finished) VALUES ({customer_id}, {courier_id}, '{message}', {is_finished})
                """
                print(sql_query)
                cur.execute(sql_query)

if __name__ == '__main__':
    pg = PgConnect('localhost', '5432', 'postgres', 'postgres', pw=None, sslmode='disable')
    OrdersTable(pg).create_order(1, 2, 'pizda')