from sqlalchemy.orm import Session
from models import Transaction

def save_transaction(db: Session, tx_data: dict):
    db_tx = Transaction(**tx_data)
    db.add(db_tx)
    db.commit()
    db.refresh(db_tx)
    return db_tx

def get_transactions_by_wallet(db: Session, wallet: str, start_date: int = None, end_date: int = None):
    query = db.query(Transaction).filter(Transaction.wallet_address == wallet)
    if start_date:
        query = query.filter(Transaction.timestamp >= start_date)
    if end_date:
        query = query.filter(Transaction.timestamp <= end_date)
    return query.all()