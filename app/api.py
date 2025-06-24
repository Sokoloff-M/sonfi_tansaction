# app/api.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import stonfi
from app.models import Transaction
from app.crud import save_transaction
from app.database import get_db

router = APIRouter()

@router.post("/fetch_swaps")
async def fetch_and_save_swaps(wallet: str, db: Session = Depends(get_db)):
    txs = await stonfi.get_swap_transactions(wallet)
    for tx in txs:
        save_transaction(db, {
            "tx_hash": tx["hash"],
            "wallet_address": wallet,
            "from_token": tx["in_msg"].get("source", ""),
            "to_token": tx["out_msgs"][0].get("destination", ""),
            "amount_in": tx["in_msg"].get("value", "0"),
            "amount_out": tx["out_msgs"][0].get("value", "0"),
            "timestamp": tx["utime"],
            "success": tx["status"] == "ok",
            "tx_type": "swap"
        })
    return {"detail": f"{len(txs)} транзакций сохранено"}