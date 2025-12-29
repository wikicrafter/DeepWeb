```text
   ___        _               ___  ____  
  / _ \ _   _| |__   ___ ___ / _ \/ ___| 
 | | | | | | | '_ \ / _ \ __| | | \___ \ 
 | |_| | |_| | |_) |  __\__ \ |_| |___) |
  \__\_\\__,_|_.__/ \___|___/\___/|____/ 
```

> root@deepweb:~# man qubes-os

### Qubes OS: A Reasonably Secure Operating System

> Security by compartmentalization. The philosophy is: "A bug in one app should not compromise the whole system."

**Architecture Concept:**
*   **Dom0 (Admin VM)**: The master controller. It has NO network access. Even if you get a virus, it can't reach Dom0 to install a persistent rootkit easily.
*   **TemplateVMs**: Read-only system files (Debian, Fedora).
*   **AppVMs**: Where you work (e.g., "personal", "work", "banking").
    *   *DisposableVMs*: Created for a single task (like opening a suspicious PDF) and **deleted** instantly after closing.

**Installation:**
1.  Download ISO from [qubes-os.org](https://www.qubes-os.org/)
2.  Flash to USB (Use `Rufus` or `dd`).
3.  Note: Qubes is picky about hardware. It needs a good CPU with VT-x/VT-d virtualization support.

---

> root@deepweb:~# ./tips.sh

### [ TIPS & TRICKS ]
*   **Whonix Integration**: Qubes comes with Whonix built-in. You can launch a "Whonix-Workstation" AppVM which forces all traffic through a "Whonix-Gateway". This is the gold standard for security.
*   **Copy/Paste**: To copy text between VMs, you must use the secure clipboard keystroke: `Ctrl+Shift+C` (global copy) and `Ctrl+Shift+V` (global paste). Normal Ctrl+C/V won't work across domains.

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
[⬅️ Previous: 0x05 Tor Install](0x05_installing_tor_on_windows.md) | [🏠 Home](../README.md) | [Next: 0x07 Tails Install ➡️](0x07_tails_os_install.md)
