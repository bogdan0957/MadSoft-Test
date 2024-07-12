from sqlalchemy import MetaData, String, Integer, Table, Column

metadata = MetaData()

memes = Table(
    "memes", metadata,
    Column("id", Integer, primary_key=True),
    Column("meme", String, nullable=False),
    Column('description', String, nullable=False)
)
