from sqlalchemy import create_engine, BigInteger, Table, Column
from sqlalchemy import text, MetaData, Connection, Integer, String, ForeignKey
from sqlalchemy.orm import Session, registry

engine = create_engine(
    "sqlite+pysqlite:///:memory:",
    echo=True,

)

# CORE METADATA

meta_data = MetaData()

user_table = Table(
    "users",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("user_id", BigInteger, unique=True),
    Column("fullname", String(30))

)

address = Table(
    "address",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey('users.user_id')),
    Column("email", String, nullable=False)

)

meta_data.create_all(engine)

with engine.connect() as conn:
    res = conn.execute(text("INSERT INTO users(user_id) VALUES (65456454546)"))

with engine.connect() as conn:
    res = conn.execute(text("SELECT * FROM users"))
    print(res.all())

meta_data.drop_all(engine)
