```text
  __  __            _        _       
 |  \/  | __ _ _ __| | _____| |_ ___ 
 | |\/| |/ _` | '__| |/ / _ \ __/ __|
 | |  | | (_| | |  |   <  __/ |_\__ \
 |_|  |_|\__,_|_|  |_|\_\___|\__|___/
```

> root@deepweb:~# wget market_list.txt

### Underground Markets Protocol

**Escrow System:**
1.  **Buyer** sends BTC to the Market (Escrow).
2.  **Vendor** ships the item.
3.  **Buyer** receives item and clicks "Finalize".
4.  **Market** releases BTC to Vendor.
*   *Safety*: If Vendor doesn't ship, Market refunds Buyer.

**The "FE" (Finalize Early) Trap:**
*   Scam vendors ask you to "Finalize Early" because "they need money for shipping" or "have low cash flow".
*   **Result**: Once you finalize, the money is gone. They never ship. **Never FE.**

**Phishing:**
*   Markets are constantly under DDoS attacks. Phishers buy google ads or spam Reddit with fake links that look real but steal your password/PIN.
*   **Defense**: Only use links from `Dark.fail` or verify the PGP signature of the login page.

---

> root@deepweb:~# ./tips.sh

### [ TIPS & TRICKS ]
*   **2FA (Two-Factor Authentication)**: Enable PGP 2FA immediately. The market will present an encrypted string; you must decrypt it to log in. This prevents phishing (phishers can't decrypt the challenge).
*   **Dispute Resolution**: If you don't receive an item, open a dispute immediately. If the timer runs out, the money auto-releases to the vendor.

/* -------------------------------------------------------------------------- */
/*                                 CONTRIBUTE                                 */
/* -------------------------------------------------------------------------- */

> root@deepweb:~# ./donate.sh --support-dev

### [ KEEP THE NETWORK ALIVE ]

> "Information wants to be free, but servers cost money."

*   **[STAR_REPO]**: Star this repository to help others discover the truth.
*   **[DEPLOY_FUNDS]**: [Access Ko-fi Gateway](https://ko-fi.com/gigaa) (Fuel the research).
*   **[SYNC_UPDATES]**: Follow on GitHub to receive the latest payloads.

> System Message: Every contribution sustains the node. Ack received. //




---
[⬅️ Previous: 0x10 Chat](0x10_chat_rooms.md) | [🏠 Home](../README.md) | [Next: 0x12 Bitcoin ➡️](0x12_intro_btc.md)
