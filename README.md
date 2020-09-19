# ArVerify
```Note: This is a proof of concept```

ArVerify is service which allows users to have their addresses verified via Google Sign On.
Verified users can then be queried or accessed via a SDK.

## Architecture
ArVerfiy is a DAO with staked auth-nodes. auth-nodes have the capability to mark an address as verified.
If an auth-node misbehaves, it will be removed from the DAO.

## Workflow
1.  User tips a fee to an auth-node
2.  User request a verification at the auth-node
3.  The auth-node returns the sign-in uri
4.  User opens this uri and signs himself up with a Google-Account
5.  The auth-node handles the callback
6.  If the Callback is successful, the auth-node writes a transaction onto arweave which states, that the address is verified
7.  The auth-node tips the DAO
8.  The auth-node returns the TX-ID of the verification TX to the user

## Usage
### Tipping to an auth-node
This is just what I came up with. I have no idea if this is a best practice.
````python
import arweave

auth_node = "..."

wallet_file_path = "my-arweave-keyfile.json"
wallet = arweave.Wallet(wallet_file_path)

fee = 0.0001
tx = arweave.Transaction(wallet, quantity=str(fee), to=auth_node)
tx.add_tag(name="App-Name", value="ArVerifyDev")
tx.add_tag(name="Type", value="Tip")
tx.sign()
tx.send()
````

In future this will be implemented into a front-end application which will handle the tipping process.

### Check if address is verified
This can be done via a GraphQL Query. It can easily be implemented into some kind
of package which can be installed into other projects.

```graphql
query transactions($authNodes: [String!], $address: String!) {
  transactions(
    owners: $authNodes
    tags: [
      { name: "App-Name", values: ["ArVerifyDev"] }
      { name: "Type", values: ["Verification"] }
      { name: "Address", values: [$address] }
    ]
  ) {
    edges {
      node {
        id
        tags {
          name
          value
        }
      }
    }
  }
}
```
## Help needed
*   More architectural guidance
*   How to implement a good tipping mechanism?
*   How to create and interact with a DAO?
*   New features

## Ideas
*   Adding this project into WeaveID
*   Having a check-sign next to address to see that the address is verified (e.g instagram)
*   Implement more auth-provider