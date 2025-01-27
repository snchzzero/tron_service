"""Main API methods"""

import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from const import GET_LIST_DATA_WALLET_LIMIT
from database import async_session_local, init_db
from models import WalletRequest, WalletRequestResponse
from tron_client import get_tron_data

app = FastAPI()


class RequestWallet(BaseModel): address: str

# def get_db():
#     db = async_session_local
#     try:
#         yield db
#     finally:
#         db.close()
#
# @app.on_event("startup")
# async def on_startup():
#     await init_db()


@app.post("/wallet/")
async def add_data_wallet(request: RequestWallet):
    tron_data = await get_tron_data(request.address)
    async with async_session_local() as session:
        wallet_request = WalletRequest(
            wallet_address=request.address,
            bandwidth=tron_data["bandwidth"],
            energy=tron_data["energy"],
            trx_balance=tron_data["trx_balance"],
            timestamp=datetime.datetime.now()
        )
        session.add(wallet_request)
        await session.commit()
    return wallet_request


@app.get("/wallets/", response_model=List[WalletRequestResponse])
async def get_list_data_wallet(skip: int = 0, limit: int = GET_LIST_DATA_WALLET_LIMIT):
    async with async_session_local() as session:
        result = await session.execute(
            WalletRequest.__table__.select().order_by(
                WalletRequest.timestamp.desc()
            ).offset(skip).limit(limit)
        )
        rows_as_dicts = [dict(row) for row in result.mappings()]
        return rows_as_dicts
