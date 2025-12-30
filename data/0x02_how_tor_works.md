```text
  ________  ____  
 |_   _/ _ \|  _ \ 
   | || | | | |_) |
   | || |_| |  _ < 
   |_| \___/|_| \_\
```

> root@deepweb:~# traceroute --tor-network target

### Network Topology: The Onion Router

Tor protects your identity by wrapping your data in layers of encryption, like an **onion**. It routes your traffic through a volunteer overlay network consisting of thousands of relays.

#### The Circuit (3 Hops)
Every connection you make typically involves 3 nodes. Why 3?
*   **1 node**: Knowing source and destination (VPN model).
*   **2 nodes**: The first node knows you, the second knows the destination. If they collude, you are de-anonymized.
*   **3 nodes**: Separate knowledge of source and destination.

```mermaid
graph LR
    User[Client (You)] -- "Encrypted (Level 3)" --> Entry[Entry Guard]
    Entry -- "Encrypted (Level 2)" --> Middle[Middle Relay]
    Middle -- "Encrypted (Level 1)" --> Exit[Exit Relay]
    Exit -- "Decrypted (Cleartext)" --> Internet[Destination Server]
```

1.  **Entry Guard**:
    *   Knows: Your IP Address.
    *   Does NOT know: The content of your traffic or the destination.
    *   *Note*: This node stays the same for months to protect against statistical attacks.

2.  **Middle Relay**:
    *   Knows: The Entry Guard and the Exit Relay.
    *   Does NOT know: Your IP, the destination, or the content.

3.  **Exit Relay**:
    *   Knows: The destination.
    *   Does NOT know: Your IP.
    *   *Risk*: The Exit Relay sees the actual data if you are not using HTTPS. **This is why HTTPS is crucial even on Tor.**

---

> root@deepweb:~# ./tips.sh

### [ TIPS & TRICKS ]
*   **Don't Torrent over Tor**: It slows down the network for everyone and leaks your real IP address in the UDP packets.
*   **HTTPS Everywhere**: If you visit a clear web site (e.g., Facebook) via Tor, ensure it is HTTPS. If it's HTTP, the Exit Relay can sniff your password.

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
[⬅️ Previous: 0x01 Myths](0x01_myths_and_misconceptions.md) | [🏠 Home](../README.md) | [Next: 0x03 PGP ➡️](0x03_what_is_pgp.md)
