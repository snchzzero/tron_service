"""Test main methods API Tron service"""

import pytest
from fastapi.testclient import TestClient
from const import TABLE_WALLET_BANDWIDTH, TABLE_WALLET_ENERGY, \
    TABLE_WALLET_TRX_BALANCE, GET_LIST_DATA_WALLET_LIMIT, TABLE_WALLET_ID, \
    TABLE_WALLET_WALLET_ADDRESS
from main import app
from .const_test import RESULT_ACCOUNT_INFO_LIST, TEST_COUNT_ACCOUNT_INFO, \
    FREE_NET_USAGE_LIST, BALANCE_LIST, \
    FROZEN_BALANCE_FOR_ENERGY
from .fixture import mock_tron, session, engine
from http import HTTPStatus


client = TestClient(app, backend='asyncio')


@pytest.mark.asyncio
async def test_post_add_data_wallet(mock_tron, session):
    """
    Test add data wallet, when:
     - get wallet info from tron client
     - handler gotten tron data and add data wallet local bd
    """

    # ARRANGE

    mock_tron.return_value = RESULT_ACCOUNT_INFO_LIST[0]

    expected_wallet_id = 1
    wallet_address = "some_new_url"

    # ACT

    response = client.post("/wallet/", json={"address": wallet_address})
    resp_data = response.json()

    # ASSERT

    assert response.status_code == HTTPStatus.OK
    assert resp_data[TABLE_WALLET_ID] == expected_wallet_id
    assert resp_data[TABLE_WALLET_WALLET_ADDRESS] == wallet_address


@pytest.mark.asyncio
async def test_get_list_data_wallet(mock_tron):
    """ Test method get_list_data_wallet when ensure gotten last 10 records from bd"""

    # ARRANGE

    unexpected_wallet = {
        TABLE_WALLET_BANDWIDTH: FREE_NET_USAGE_LIST[0],
        TABLE_WALLET_ENERGY: FROZEN_BALANCE_FOR_ENERGY[0],
        TABLE_WALLET_TRX_BALANCE: BALANCE_LIST[0]
    }

    for test_count in range(TEST_COUNT_ACCOUNT_INFO):
        mock_tron.return_value = RESULT_ACCOUNT_INFO_LIST[test_count]
        client.post("/wallet/", json={"address": "some_url"})

    # ACT

    response = client.get("/wallets/")
    resp_data_list = response.json()

    # ASSERT

    assert response.status_code == HTTPStatus.OK
    assert len(resp_data_list) == GET_LIST_DATA_WALLET_LIMIT
    assert all(
        [wallet[TABLE_WALLET_BANDWIDTH] != unexpected_wallet[TABLE_WALLET_BANDWIDTH]
         for wallet in resp_data_list]
    )
    assert all(
        [wallet[TABLE_WALLET_ENERGY] != unexpected_wallet[TABLE_WALLET_ENERGY]
         for wallet in resp_data_list]
    )
    assert all(
        [wallet[TABLE_WALLET_TRX_BALANCE] != unexpected_wallet[TABLE_WALLET_TRX_BALANCE]
         for wallet in resp_data_list]
    )
