import arweave
from simple_graphql_client import GraphQLClient, load

wallet_file_path = "arweave-keyfile.json"
wallet = arweave.Wallet(wallet_file_path)

gql_client = GraphQLClient(base_url="https://arweave.dev/graphql")


def tip_received(owner: str, fee: float) -> bool:
    recipient = wallet.address
    query = load("queries/tipped.gql")
    variables = {
        "owner": owner,
        "recipient": recipient
    }
    response = gql_client.query(query, variables)
    edges = response['data']['transactions']['edges']
    node = edges[0]['node']
    quantity = float(node['quantity']['ar'])
    return quantity == fee


# def select_from_contract():
#    return "..."


def send_to_arweave(verified_address: str, fee: float) -> arweave.Transaction:
    # store verification on chain
    transaction = arweave.Transaction(wallet)
    transaction.add_tag(name="AppName", value="ArVerifyDev")
    transaction.add_tag(name="verified", value=verified_address)
    transaction.sign()
    _fee = transaction.get_price()
    transaction.send()

    # tip member of DAO
    # fee -= _fee
    # print("_fee", _fee)
    # print("fee", fee)
    # to_address = select_from_contract()
    # tip_transaction = arweave.Transaction(wallet, quantity=fee, to=to_address)
    # tip_transaction.add_tag(name="AppName", value="ArVerifyDev")
    # tip_transaction.sign()
    # tip_transaction.send()

    return transaction
