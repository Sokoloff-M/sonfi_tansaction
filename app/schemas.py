from pydantic import BaseModel

class TransactionRequest(BaseModel):
    wallet: str
    start_date: int | None = None
    end_date: int | None = None