```text
 __        ___           _                    
 \ \      / (_)_ __   __| | _____      _____  
  \ \ /\ / /| | '_ \ / _` |/ _ \ \ /\ / / __| 
   \ V  V / | | | | | (_| | (_) \ V  V /\__ \ 
    \_/\_/  |_|_| |_|\__,_|\___/ \_/\_/ |___/ 
```

> root@deepweb:~# systemctl status windows_os

**Status: INSECURE [CRITICAL WARNING]**

> **Do NOT use Windows on the Deep Web for anything sensitive.**

### The "Why" - Technical Breakdown
Windows is a Closed Source operating system. We do not know what the code does, but independent analysis has shown:

1.  **Telemetry**: Windows 10/11 sends massive amounts of usage data to Microsoft (and by extension, the NSA via PRISM).
    *   *Examples*: Cortana voice data, typing history, app usage, location history.
2.  **Registry Leaks**: Even if you think you deleted a file, the Windows Registry often keeps a record of it having existed (ShellBags).
3.  **Thumbnails**: Windows caches images of everything you view in `thumbs.db`. Even if you delete the image, the thumbnail remains.
4.  **Swap File**: Windows writes RAM to the hard drive (`pagefile.sys`). Sensitive data remains on disk forensically.

### If You MUST Use Windows (Low Threat Model)
If you are just browsing out of curiosity and doing nothing illegal:
1.  **Disable Telemetry**: Use tools like *O&O ShutUp10++*.
2.  **Full Disk Encryption**: Use **Veracrypt** (since BitLocker keys are often backed up to your Microsoft Account).
3.  **No Admin**: Run Tor Browser as a standard user, not Administrator.

---

> root@deepweb:~# ./tips.sh

### [ TIPS & TRICKS ]
*   **Virtual Machines**: If you are on Windows, download VirtualBox and run **Whonix** inside it. This isolates the Tor connection from your host reading specific data.
*   **The "3-Click" Rule**: If you accidentally download a file on Windows, you are 3 clicks away from being owned. Don't open ANY downloaded files (PDF, DOCX) while online.

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
[⬅️ Previous: 0x03 PGP](0x03_what_is_pgp.md) | [🏠 Home](../README.md) | [Next: 0x05 Install ➡️](0x05_installing_tor_on_windows.md)
