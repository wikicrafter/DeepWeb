```text
  ____   ____ ____  
 |  _ \ / ___|  _ \ 
 | |_) | |  _| |_) |
 |  __/| |_| |  __/ 
 |_|    \____|_|    
```

> root@deepweb:~# gpg --version

### Pretty Good Privacy (PGP)

> **Definition**: Protocol for encrypting, signing, and decrypting texts, e-mails, files, directories, and whole disk partitions and to increase the security of e-mail communications.

**Why it's Mandatory on the Deep Web:**
Only PGP ensures that the admin of the marketplace, the ISP, or the government cannot read your messages to a vendor.

### Asymmetric Encryption 101
*   **Public Key**: You give this to everyone. "This is my open mailbox."
*   **Private Key**: You keep this safe. "This is the key to open my mailbox."

> **Scenario**: You want to send your address to a Vendor.
> 1. Find Vendor's **Public Key** on their profile.
> 2. Import it into your keyring.
> 3. Encrypt your address using their Public Key.
> 4. Send the resulting block of garbled text.
> 5. Only the Vendor (holder of the Private Key) can decrypt it.

### CLI Quick Reference (Linux/GPG)

```bash
# Generate a new keypair (Select RSA and 4096 bits)
gpg --full-generate-key

# Import someone's public key
gpg --import vendor_key.asc

# Encrypt a message for recipient "VendorName"
gpg --encrypt --armor --recipient VendorName message.txt

# Decrypt a message sent to you
gpg --decrypt encrypted_message.asc
```

---

> root@deepweb:~# ./tips.sh

### [ TIPS & TRICKS ]
*   **Never decrypt online**: Never paste your private key into a website offering "Online PGP Decryption". It is a phishing tactic.
*   **Verification**: Always sign your messages to prove they came from you.
*   **Clipboards**: Be careful copying private keys. Malware monitors clipboards.

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
**[⬅️ Previous: 0x02 Tor](0x02_how_tor_works.md)** | **[🏠 Home](../README.md)** | **[Next: 0x04 Windows Warning ➡️](0x04_dont_use_windows.md)**
