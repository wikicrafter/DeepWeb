```text
  _     _                  
 | |   (_)_ __  _   ___  __
 | |   | | '_ \| | | \ \/ /
 | |___| | | | | |_| |>  < 
 |_____|_|_| |_|\__,_/_/\_\
```

> root@deepweb:~# cat /etc/distros

### Distro Comparison Matrix

Choosing the right OS depends on your threat model.

| Feature | Tails OS | Whonix | Qubes OS | Kali Linux |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Goal** | Amnesia (Forgetting) | Anonymity (Isolation) | Security (Isolation) | Offense (Hacking) |
| **Persistance** | No (Default) | Yes | Yes | Yes |
| **VM Required** | No (USB Boot) | Yes (VirtualBox) | Bare Metal | Bare Metal/VM |
| **Tor Enforcement** | System-wide | System-wide (Gateway) | Configurable | No |
| **Best For** | Journalists, Burner usage | Daily use, Hosting | Power Users, Experts | Pentesters (NOT privacy) |

**Recommendation:**
*   **Beginner**: Use **Tails**. It's fool-proof. If you pull the USB, the data is gone.
*   **Intermediate**: Use **Whonix** inside VirtualBox on your main PC.
*   **Expert**: **Qubes OS**.

---

> root@deepweb:~# ./tips.sh

### [ TIPS & TRICKS ]
*   **Why not Kali?**: Everyone thinks "Hacker = Kali". However, Kali is designed to be LOUD and attack networks. It is **terrible** for privacy. By default, it runs as root and doesn't route through Tor. Do not use Kali for deep web browsing.

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
[⬅️ Previous: 0x08 Tails](0x08_tails_os_overview.md) | [🏠 Home](../README.md) | [Next: 0x0A Nuances ➡️](0x0A_deep_web_nuances.md)
