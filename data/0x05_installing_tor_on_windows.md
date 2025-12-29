```text
  ___           _        _ _ 
 |_ _|_ __  ___| |_ __ _| | |
  | || '_ \/ __| __/ _` | | |
  | || | | \__ \ || (_| | | |
 |___|_| |_|___/\__\__,_|_|_|
```

> root@deepweb:~# apt install tor-browser

### Installation Guide (Windows)

> [!CAUTION]
> Installing on Windows is not recommended for high-threat models. If you are buying on darknet or leaking any secrets, STOP. Go to [0x07_tails_os_install.md](0x07_tails_os_install.md).
> If you are just browsing: Proceed.

1.  **Download**: Navigate to [TorProject.org](https://www.torproject.org/download/)
    *   *Warning*: Never download from 3rd party sites (CNET, Softonic). They bundle malware.
2.  **Verify**: Check the GPG signature.
    *   The Tor Project signs their releases. If you skip this, you might be installing a trojaned version.
3.  **Install**: Run the binary (`torbrowser-install-win64-xxx.exe`).

### Hardening Tips (If you MUST use Windows)
*   **Discord/Steam**: Close them completely. They scan running processes and can report "Tor Browser" to their telemetry.
*   **Window Size**: Do not maximize the Tor Browser window. It changes your fingerprint (resolution) which makes you unique. Keep it default.
*   **VPN**: Do **NOT** use a free VPN with Tor. It adds a point of failure.

---

> root@deepweb:~# ./tips.sh

### [ TIPS & TRICKS ]
*   **Bridges**: If Tor is blocked in your country (or by your ISP), use a "Bridge" during setup (Select "Tor is censored in my country").
*   **Snowflake**: Use the Snowflake bridge to look like you are on a video call instead of using Tor.

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
[⬅️ Previous: 0x04 Windows](0x04_dont_use_windows.md) | [🏠 Home](../README.md) | [Next: 0x06 Qubes ➡️](0x06_qubes_os_install.md)
