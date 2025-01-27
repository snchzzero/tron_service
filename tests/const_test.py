"""Constants for tests"""

TEST_COUNT_ACCOUNT_INFO = 11
FREE_NET_USAGE_LIST = [
    1000,
    2000,
    3000,
    4000,
    5000,
    6000,
    7000,
    8000,
    9000,
    101010,
    202020
]
FROZEN_BALANCE_FOR_ENERGY = [
    1100000,
    2200000,
    3300000,
    4400000,
    5500000,
    6600000,
    7700000,
    8800000,
    9900000,
    1111111,
    2222222
]
BALANCE_LIST = [
    1000000,
    2000000,
    3000000,
    4000000,
    5000000,
    6000000,
    7000000,
    8000000,
    9000000,
    10000000,
    11000000
]

RESULT_ACCOUNT_INFO_LIST = [
    {
        "account_resource": {
            "freeNetUsage": FREE_NET_USAGE_LIST[test_count],
            "frozen_balance_for_energy": FROZEN_BALANCE_FOR_ENERGY[test_count]
        },
        "balance": BALANCE_LIST[test_count]
    } for test_count in range(TEST_COUNT_ACCOUNT_INFO)
]
