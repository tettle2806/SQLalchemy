from sqlalchemy import create_engine, Column, ForeignKey, String, Integer, BigInteger
from sqlalchemy.orm import Mapped, registry, mapped_column, declarative_base, as_declarative, declared_attr
from sqlalchemy.orm import Session
from sqlalchemy import select

engine = create_engine(
    "sqlite+pysqlite:///:memory:",
    echo=True
)


# Base = declarative_base()


@as_declarative()
class AbstractModel:
    id:Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class UserModel(AbstractModel):
    __tablename__ = 'users'
    user_id: Mapped[int] = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column()
    fullname: Mapped[str] = mapped_column()


class AddressModel(AbstractModel):
    __tablename__ = 'address'
    email = mapped_column(String, nullable=True)
    user_id = mapped_column(ForeignKey('users.id'))


print(UserModel.__table__.__dict__)
print(AddressModel.__table__)

with Session(engine) as session:
    with session.begin():
        AbstractModel.metadata.create_all(engine)
        user = UserModel(user_id=1, name='ZIdan',fullname='RASULOV ZAYNIDDIN')
        session.add(user)

    with session.begin():
        result = session.execute(select(UserModel).where(UserModel.user_id == 1))
        print(result.scalar())
