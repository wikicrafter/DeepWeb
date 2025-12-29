```text
  _   _           _   _             
 | | | | ___  ___| |_(_)_ __   __ _ 
 | |_| |/ _ \/ __| __| | '_ \ / _` |
 |  _  | (_) \__ \ |_| | | | | (_| |
 |_| |_|\___/|___/\__|_|_| |_|\__, |
                              |___/ 
```

> root@deepweb:~# service tor start

### Hosting Hidden Services (.onion)

**The Risks:**
Hosting a Tor site makes you a target. If your server is misconfigured, it leaks your Real IP.
*   **Correlation Attack**: If your server is online 24/7 on your home IP, the ISP sees "Tor Traffic" 24/7.
*   **Deanonymization**: Apache/Nginx default error pages often reveal the server version and OS.

**Hardening Checklist:**
1.  **Disable Server Tokens**: Edit `nginx.conf` -> `server_tokens off;`.
2.  **Bind to Localhost**: Ensure your web server ONLY listens on `127.0.0.1`. If it listens on `0.0.0.0`, it might be accessible from the clear web.
3.  **Use a VPS**: Never host from home. Buy a VPS using Monero from a provider that ignores DMCA (e.g., in Moldova, Russia, or offshore).

---

> root@deepweb:~# ./tips.sh

### [ TIPS & TRICKS ]
*   **OnionScan**: A tool (like Nmap) for onion sites. Run it against your own site to find vulnerabilities.
*   **Static Sites**: If possible, use a static site generator (Hugo/Jekyll). Databases (MySQL) are major attack vectors (SQL Injection).

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
**[?? Previous: 0x18 GPG](0xFFFFFFFF*.md)** | **[?? Home](../README.md)** | **[Next: 0x1A Mobile ??](0x01*.md)**

---
**[⬅️ Previous: 0x18 GPG](0x18_gpg4win.md)** | **[🏠 Home](../README.md)** | **[Next: 0x1A Mobile ➡️](0x1A_mobile_deep_web.md)**
