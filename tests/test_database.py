"""Test add and get data from database"""

import datetime
import pytest
from const import TABLE_WALLET_WALLET_ADDRESS, TABLE_WALLET_BANDWIDTH, \
    TABLE_WALLET_TRX_BALANCE, TABLE_WALLET_ENERGY, \
    TABLE_WALLET_TRX_TIMESTAMP, TABLE_WALLET_ID
from .fixture import session, engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import WalletRequest


@pytest.mark.asyncio
async def test_query_add_get_data_from_database(session: AsyncSession):
    """Test query add and get wallet data from local database"""

    # ARRANGE

    time_now = datetime.datetime.now()
    wallet_address = "some_wallet_address"
    expected_result = [
        {
            TABLE_WALLET_ID: 1,
            TABLE_WALLET_WALLET_ADDRESS: wallet_address,
            TABLE_WALLET_BANDWIDTH: '100',
            TABLE_WALLET_ENERGY: '200',
            TABLE_WALLET_TRX_BALANCE: '5.7',
            TABLE_WALLET_TRX_TIMESTAMP: time_now
        }
    ]

    async with session.begin():
        wallet_request = WalletRequest(
            wallet_address=wallet_address,
            bandwidth='100',
            energy='200',
            trx_balance='5.7',
            timestamp=time_now
        )
        session.add(wallet_request)

    # ACT

    query = select(WalletRequest).with_only_columns(WalletRequest.__table__.columns)
    result_all = await session.execute(query)
    rows_as_dicts = [dict(row) for row in result_all.mappings()]

    # ASSERT

    assert rows_as_dicts == expected_result
