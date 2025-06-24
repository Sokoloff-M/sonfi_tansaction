# app/stonfi.py
import httpx
from fastapi import HTTPException

STONFI_CONTRACT_MAINNET = "EQB3ncyBUTjZUA5EnFKR5_EnOMI9V1tTEAAPaiU71gc4TiUt"

async def get_swap_transactions(wallet_addr: str):
    url = f"https://toncenter.com/api/v2/getTransactions?address={wallet_addr}&limit=100"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Не удалось получить транзакции")

        data = response.json().get("result", [])
        
        swaps = []
        for tx in data:
            if tx["in_msg"] and STONFI_CONTRACT_MAINNET in tx["in_msg"].get("source", ""):
                swaps.append(tx)
            elif any(STONFI_CONTRACT_MAINNET in msg.get("destination", "") for msg in tx["out_msgs"]):
                swaps.append(tx)

        return swaps