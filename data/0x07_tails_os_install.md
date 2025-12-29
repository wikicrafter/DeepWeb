```text
  _____     _ _       
 |_   _|_ _(_) |___   
   | |/ _` | | / __|  
   | | (_| | | \__ \  
   |_|\__,_|_|_|___/  
```

> root@deepweb:~# dd if=tails.iso of=/dev/sdb bs=4M status=progress

### Tails: The Amnesic Incognito Live System

> "Leave no trace."
> Tails is a live OS that you boot from a USB stick. It forces all connections through Tor and forgets everything when you shut down.

**Prerequisites:**
*   A USB Stick (min 8GB).
*   [Tails ISO](https://tails.boum.org/).
*   Verification Tool (GPG or the Tails Verification extension).

**Procedure:**
1.  **Download**: Get the image.
2.  **VERIFY (CRITICAL)**:
    *   If you download a compromised version of Tails, your anonymity is zero.
    *   Use the [browser verification tool](https://tails.boum.org/install/index.en.html) or `gpg --verify tails.iso.sig tails.iso`.
3.  **Flash**: Use **BalenaEtcher** (Windows/Mac) or `gnome-disks` (Linux).
4.  **Boot**: Insert USB, restart computer, and mash the Boot Menu key (`F12`, `F2`, or `Del`).

---

> root@deepweb:~# ./tips.sh

### [ TIPS & TRICKS ]
*   **Persistence**: You can configure an encrypted partition on the USB stick to save PGP keys and KeePass databases. (Applications -> Configure Persistent Volume).
*   **Camouflage**: Tails has a "Windows 10 Camouflage" mode that makes the desktop look like Windows 10 to casual passersby (e.g., in a coffee shop).

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
[⬅️ Previous: 0x06 Qubes](0x06_qubes_os_install.md) | [🏠 Home](../README.md) | [Next: 0x08 Tails Overview ➡️](0x08_tails_os_overview.md)
