# ArVerify
ArVerify is service which allows users to let their addresses verified via Google Sign On.
Verified users can then be queried or accessed via a SDK.

## Architecture
ArVerfiy is a DAO with staked authposts. Authposts have the capability to mark an address as verified.
If an authpost misbehaves, it will be removed from the DAO.

## Workflow
1.  User tips a fee to an authpost
2.  User request a verification at the authpost
3.  The authpost returns the sign-in uri
4.  User opens this uri and signs himself up with a Google-Account
5.  The authpost handles the callback
6.  If the Callback is successful, the authpost writes a transaction onto arweave which states, that the address is verified
7.  The authpost tips the DAO
8.  The authpost returns the TX-ID of the verification TX to the user