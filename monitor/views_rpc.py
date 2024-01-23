import json

import requests
from django.http import JsonResponse
from NanoMonitor.settings import RPC_URL, UNSAFE_RPC_ENABLED


def rpc_request(payload: dict) -> json:
    data = requests.post(RPC_URL, data=json.dumps(payload))
    print(data.text)
    if data.status_code == 200:
        return data.json()
    else:
        return {'error': 'Request failed'}

def rpc_call(unsafe: bool, unconfirmed: bool):
    def unsafe_rpc_handler(func):
        if unconfirmed:
            print("Warning this method returns unconfirmed blocks. ")
        # unsafe rpc calls can allow access to node wallet and potentiall shut it down.
        if unsafe:
            print("Warning this method is labeled as unsafe. it could return unconfirmed blocks")
            if UNSAFE_RPC_ENABLED:
                return func
            else:
                print("This rpc call is currently disabled.")
        else:
            # just run if its safe.
            return func

    return unsafe_rpc_handler


@rpc_call(unsafe=False, unconfirmed=False)
def account_balance():
    """
    :param wallet_address:
    :return:
    {
      "balance": "10000",
      "pending": "10000",
      "receivable": "10000"
    }
    """
    payload = {
        "action": "account_balance",
    }
    return rpc_request(payload)


@rpc_call(unsafe=False, unconfirmed=False)
def account_block_count(wallet_address: str):
    """
    :param wallet_address:
    :return:

    """
    payload = {
        "action": "account_block_count",
        "account": wallet_address
    }
    return rpc_request(payload)


@rpc_call(unsafe=False, unconfirmed=False)
def account_get(public_key: str):
    """
    :param wallet_address:
    :return:
    """
    payload = {
        "action": "account_get",
        "key": public_key
    }
    return rpc_request(payload)


@rpc_call(unsafe=False, unconfirmed=True)
def account_history(account: str, count: int):
    """
    Reports send/receive information for an account.
    :param wallet_address:
    :return:
    """
    payload = {
        "action": "account_history",
        "account": account,
        'count': count
    }
    return rpc_request(payload)


@rpc_call(unsafe=False, unconfirmed=True)
def account_info(account: str, count: int):
    """
    Reports send/receive information for an account.
    :param :
    :return:
    """
    payload = {
        "action": "account_history",
        "account": account,
        'count': count
    }
    return rpc_request(payload)


@rpc_call(unsafe=False, unconfirmed=False)
def account_key(account: str):
    payload = {
        "action": "account_key",
        "account": account,
    }
    return rpc_request(payload)


@rpc_call(unsafe=False, unconfirmed=False)
def account_representative(account: str):
    payload = {
        "action": "account_representative",
        "account": account,
    }
    return rpc_request(payload)


@rpc_call(unsafe=False, unconfirmed=False)
def account_weight(account: str):
    payload = {
        "action": "account_weight",
        "account": account,
    }
    return rpc_request(payload)


@rpc_call(unsafe=False, unconfirmed=True)
def account_balances(accounts: [str]):
    payload = {
        "action": "accounts_balances",
        "accounts": accounts,
    }
    return rpc_request(payload)


@rpc_call(unsafe=False, unconfirmed=True)
def account_frontiers(accounts: [str]):
    payload = {
        "action": "accounts_frontiers",
        "accounts": accounts,
    }
    return rpc_request(payload)


@rpc_call(unsafe=False, unconfirmed=False)
def accounts_receivable(accounts: [str], count: int = 1):
    payload = {
        "action": "accounts_receivable",
        "accounts": accounts,
        "count": count
    }
    return rpc_request(payload)


@rpc_call(unsafe=False, unconfirmed=False)
def accounts_representatives(accounts: [str]):
    payload = {
        "action": "accounts_representatives",
        "accounts": accounts
    }
    return rpc_request(payload)


@rpc_call(unsafe=False, unconfirmed=False)
def available_supply():
    payload = {
        "action": "available_supply",
    }
    return rpc_request(payload)


@rpc_call(unsafe=False, unconfirmed=False)
def block_account(hash_string : str):
    payload = {
        "action": "block_account",
        "hash": hash_string
    }
    return rpc_request(payload)


@rpc_call(unsafe=False, unconfirmed=False)
def block_confirm(hash_string : str):
    payload = {
        "action": "block_confirm",
        "hash": hash_string
    }
    return rpc_request(payload)


@rpc_call(unsafe=False, unconfirmed=False)
def block_count():
    payload = {
        "action": "block_count",
    }
    return rpc_request(payload)


@rpc_call(unsafe=True, unconfirmed=False)
def block_create():
    #TODO UNDONE.
    payload = {
        "action": "block_create",
        "json_block": "true",
        "type": "state",
        "balance": "1000000000000000000000",
        "key": "0000000000000000000000000000000000000000000000000000000000000002",
        "representative": "nano_1hza3f7wiiqa7ig3jczyxj5yo86yegcmqk3criaz838j91sxcckpfhbhhra1",
        "link": "19D3D919475DEED4696B5D13018151D1AF88B2BD3BCFF048B45031C1F36D1858",
        "previous": "F47B23107E5F34B2CE06F562B5C435DF72A533251CB414C51B2B62A8F63A00E4"
    }
    return rpc_request(payload)


@rpc_call(unsafe=False, unconfirmed=False)
def block_hash(block: dict, json_block: bool = True ):
    payload = {
        "action": "block_hash",
        "json_block": json_block,
        "block": block
   }
    return rpc_request(payload)

@rpc_call(unsafe=False, unconfirmed=False)
def block_info(block: dict, json_block: bool = True ):
    payload = {
        "action": "block_hash",
        "json_block": json_block,
        "block": block
   }
    return rpc_request(payload)

@rpc_call(unsafe=False, unconfirmed=False)
def blocks(hashes: [str], json_block: bool = True ):
    payload = {
        "action": "blocks",
        "json_block": json_block,
        "hashes": hashes
   }
    return rpc_request(payload)


@rpc_call(unsafe=False, unconfirmed=False)
def blocks_info(hashes: [str], json_block: bool = True ):
    # TODO OPTIONAL ARGUEMENTS
    payload = {
        "action": "blocks",
        "json_block": json_block,
        "hashes": hashes
   }
    return rpc_request(payload)




def get_uptime():
    """
    average count of blocks in ledger (including unconfirmed)
    :return:
    """
    payload = {
        "action": "uptime"
    }
    return rpc_request(payload)


def get_block_count():
    """
    average count of blocks in ledger (including unconfirmed)
    :return:
    """
    payload = {
        "action": "block_count"
    }
    return rpc_request(payload)


def get_telemetry() -> json:
    """
    block_count	average count of blocks in ledger (including unconfirmed)
    cemented_count	average count of blocks cemented in ledger (only confirmed)
    unchecked_count	average count of unchecked blocks. This should only be considered an estimate as nodes running RocksDB may not return exact counts.
    account_count	average count of accounts in ledger
    bandwidth_cap	0 = unlimited; the mode is chosen if there is more than 1 common result otherwise the results are averaged (excluding 0)
    peer_count	average count of peers nodes are connected to
    *_version	mode (most common) of (protocol, major, minor, patch, pre_release) versions
    uptime	average number of seconds since the UTC epoch at the point where the response is sent from the peer
    genesis_block	mode (most common) of genesis block hashes
    maker	mode (most common), meant for third party node software implementing the protocol so that it can be distinguished, 0 = Nano Foundation, 1 = Nano Foundation pruned node
    timestamp	number of milliseconds since the UTC epoch at the point where the response is sent from the peer
    active_difficulty	V22.0+ returns minimum network difficulty due to deprecated active difficulty measurements

    up to V21.3 returns average of the current network difficulty, see active_difficulty "network_current"
    :return:
    {
    "block_count": "5777903",
    "cemented_count": "688819",
    "unchecked_count": "443468",
    "account_count": "620750",
    "bandwidth_cap": "1572864",
    "peer_count": "32",
    "protocol_version": "18",
    "uptime": "556896",
    "genesis_block": "F824C697633FAB78B703D75189B7A7E18DA438A2ED5FFE7495F02F681CD56D41",
    "major_version": "21",
    "minor_version": "0",
    "patch_version": "0",
    "pre_release_version": "0",
    "maker": "0",
    "timestamp": "1587055945990",
    "active_difficulty": "fffffff800000000"
    }
    """
    payload = {
        "action": "telemetry"
    }
    return rpc_request(payload)


def get_stats_counters() -> json:
    """

    :return:
    """
    payload = {
        "action": "stats",
        "type": "counters"
    }
    return rpc_request(payload)


def get_account_balance(account: str) -> json:
    """
    Get balance for a given account wallet address
    :return:
    {
  "balance": "10000",
  "pending": "10000",
  "receivable": "10000"
}
    """
    payload = {
        "action": "account_balance",
        "account": account
    }
    return rpc_request(payload)


def block_info(hash: str) -> json:
    """
    Retrieves a json representation of the block in contents along with:
        since version 18.0: block_account, transaction amount, block balance, block height in account chain, block local modification timestamp
        since version 19.0: Whether block was confirmed, subtype (for state blocks) of send, receive, change or epoch
        since version 23.0: successor returned
        Using the optional json_block is recommended since v19.0.
    :param hash:
    :return:
            {
          "block_account": "nano_1ipx847tk8o46pwxt5qjdbncjqcbwcc1rrmqnkztrfjy5k7z4imsrata9est",
          "amount": "30000000000000000000000000000000000",
          "balance": "5606157000000000000000000000000000000",
          "height": "58",
          "local_timestamp": "0",
          "successor": "8D3AB98B301224253750D448B4BD997132400CEDD0A8432F775724F2D9821C72",
          "confirmed": "true",
          "contents": {
            "type": "state",
            "account": "nano_1ipx847tk8o46pwxt5qjdbncjqcbwcc1rrmqnkztrfjy5k7z4imsrata9est",
            "previous": "CE898C131AAEE25E05362F247760F8A3ACF34A9796A5AE0D9204E86B0637965E",
            "representative": "nano_1stofnrxuz3cai7ze75o174bpm7scwj9jn3nxsn8ntzg784jf1gzn1jjdkou",
            "balance": "5606157000000000000000000000000000000",
            "link": "5D1AA8A45F8736519D707FCB375976A7F9AF795091021D7E9C7548D6F45DD8D5",
            "link_as_account": "nano_1qato4k7z3spc8gq1zyd8xeqfbzsoxwo36a45ozbrxcatut7up8ohyardu1z",
            "signature": "82D41BC16F313E4B2243D14DFFA2FB04679C540C2095FEE7EAE0F2F26880AD56DD48D87A7CC5DD760C5B2D76EE2C205506AA557BF00B60D8DEE312EC7343A501",
            "work": "8a142e07a10996d5"
          },
          "subtype": "send"
        }
    """
    payload = {
        "action": "block_info",
        "json_block": "true",
        "hash": hash
    }
    return rpc_request(payload)




def get_available_supply() -> json:
    """"
    Returns how many raw are in the public supply
    """
    payload = {
        "action": "available_supply"
    }
    return rpc_request(payload)


def get_delegators_count(account: str):
    """
    Get number of delegators for a specific representative account
    :return:
    {
      "count": "2"
    }
    """
    payload = {
        "action": "delegators_count",
        "account": account
    }
    return rpc_request(payload)


def get_frontier_count() -> json:
    """
    Reports the number of accounts in the ledger
    :return:
    {
  "count": "920471"
}
    """
    payload = {
        "action": "frontier_count"
    }

    return rpc_request(payload)


def get_representatives_online(weight: bool = False):
    """
    Returns a list of online representative accounts that have voted recently
    :return:
    {
      "representatives": [
        "nano_1111111111111111111111111111111111111111111111111117353trpda",
        "nano_1111111111111111111111111111111111111111111111111awsq94gtecn",
        "nano_114nk4rwjctu6n6tr6g6ps61g1w3hdpjxfas4xj1tq6i8jyomc5d858xr1xi"
      ]
    }
    """
    payload = {
        "action": "representatives_online",
        "weight": weight
    }
    return rpc_request(payload)


def get_representatives(count: int = 0):
    """
    Returns a list of pairs of representative and its voting weight
    :param count: optional
    :return:
    """
    payload = {
        "action": "representatives"
    }
    # count is optional, if it exists add it to the request.
    if count > 0:
        payload.update({"count": str(count)})
    return rpc_request(payload)


def get_wallet_representative(wallet: str) -> json:
    """
    Returns the default representative for wallet
    :return:
    {
      "representative": "nano_3e3j5tkog48pnny9dmfzj1r16pg8t1e76dz5tmac6iq689wyjfpi00000000"
    }
    """
    payload = {
        "action": "wallet_representative",
        "wallet": wallet
    }
    return rpc_request(payload)
