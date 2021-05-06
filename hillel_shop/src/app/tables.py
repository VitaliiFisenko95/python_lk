import sqlalchemy as sa
metadata = sa.MetaData()

products_table = sa.Table(
    'products',

    metadata,
    sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True),
    sa.Column('name', sa.String(128)),
    sa.Column('price', sa.BigInteger),
    sa.Column('info', sa.Text),
    sa.Column('quantity', sa.BigInteger),
    sa.Column('date_created', sa.DateTime),
    sa.Column('cart_id', sa.BigInteger, nullable=True),

)

cart_table = sa.Table(
    'carts',
    metadata,
    sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True),
    sa.Column('date_created', sa.DateTime),
    sa.Column('user_id', sa.BigInteger, nullable=True),
)

user_table = sa.Table(
    'users',
    metadata,
    sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True),
    sa.Column('name', sa.String(128)),
    sa.Column('date_created', sa.DateTime),
    sa.Column('cart_id', sa.BigInteger, nullable=True),
)
