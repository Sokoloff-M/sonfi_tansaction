from sqlalchemy import Column, Integer, String, DateTime, Boolean
from database import Base  

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    tx_hash = Column(String, unique=True, index=True)
    wallet_address = Column(String, index=True)
    from_token = Column(String)
    to_token = Column(String)
    amount_in = Column(String)
    amount_out = Column(String)
    timestamp = Column(DateTime)
    success = Column(Boolean)
    tx_type = Column(String)