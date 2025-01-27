"""Service request to tron client"""

from tronpy import Tron
from const import TABLE_WALLET_BANDWIDTH, TABLE_WALLET_ENERGY, \
    TABLE_WALLET_TRX_BALANCE, TRON_CLIENT_ACCOUNT_RESOURCE, \
    TRON_CLIENT_FREE_NET_USAGE, TRON_CLIENT_FROZEN_BALANCE_FOR_ENERGY, \
    TRON_CLIENT_BALANCE

client = Tron()

async def get_tron_data(address: str) -> dict:
    """Get data from tron client by url """

    resp_account_info = client.get_account(address)

    account_info = resp_account_info[TRON_CLIENT_ACCOUNT_RESOURCE]
    free_net_usage = account_info[TRON_CLIENT_FREE_NET_USAGE]
    frozen_balance_for_energy = account_info[TRON_CLIENT_FROZEN_BALANCE_FOR_ENERGY]
    balance = float(resp_account_info[TRON_CLIENT_BALANCE] / 1e6)

    tron_data_dict = {
        TABLE_WALLET_BANDWIDTH: free_net_usage,
        TABLE_WALLET_ENERGY: frozen_balance_for_energy,
        TABLE_WALLET_TRX_BALANCE: balance
    }
    return tron_data_dict