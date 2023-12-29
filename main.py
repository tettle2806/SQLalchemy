from sqlalchemy import create_engine
from sqlalchemy import text, MetaData, Connection
from sqlalchemy.orm import Session

engine = create_engine(
    "sqlite+pysqlite:///:memory:",
    echo=True,

)

with engine.connect() as conn:
    res = conn.execute(text("SELECT 'Hello world'"))
    print(res.scalar())
