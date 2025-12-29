```text
  _   _                                   
 | \ | |_   _  __ _ _ __   ___ ___ ___    
 |  \| | | | |/ _` | '_ \ / __/ _ \ __|   
 | |\  | |_| | (_| | | | | (_|  __\__ \   
 |_| \_|\__,_|\__,_|_| |_|\___\___|___/   
```

> root@deepweb:~# nslookup site.onion

### Addressing System: The .ONION Protocol

**The Upgrade (V2 vs V3):**
*   **V2 Addresses (Deprecated)**: Short, 16 characters. Weak cryptography (RSA-1024). *These no longer work.*
*   **V3 Addresses (Standard)**: Long, 56 characters. Strong cryptography (ED25519-ECC).
    *   *Example*: `vww6ybal4bd7szmgncyruucpgfkqahzddi37ktceo3ah7ngmcopnpyyd.onion`

**Vanity Addresses:**
Hackers use brute-force generators (like `mkp224o`) to create addresses that start with readable words.
*   *Example*: `facebookwkhpil...onion`
*   *Tip*: If a market link changes but the first few letters are the same, **CHECK THE WHOLE STRING**. Phishers generate "lookalike" vanity addresses.

---

> root@deepweb:~# ./tips.sh

### [ TIPS & TRICKS ]
*   **Bookmarking**: Do not rely on "Hidden Wikis" for your links. Once you verify a site is real (e.g., via PGP signature), **Bookmark it**.
*   **Offline Storage**: Keep a text file of your verified onion links in your VeraCrypt container or Persistent Tails storage.

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
**[?? Previous: 0x09 Distros](0xFFFFFFFF*.md)** | **[?? Home](../README.md)** | **[Next: 0x0B Security ??](0x01*.md)**

---
**[⬅️ Previous: 0x09 Distros](0x09_linux_distros.md)** | **[🏠 Home](../README.md)** | **[Next: 0x0B Security ➡️](0x0B_tor_security.md)**
