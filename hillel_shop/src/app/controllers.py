from datetime import datetime

from app.db import insert_one

from app.tables import products_table


def create_product(conn, data):
    data['date_created'] = datetime.now()
    query = (
        products_table.insert().values(data).returning(products_table)
    )
    return insert_one(conn, query)
