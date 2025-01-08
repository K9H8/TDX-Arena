# Route Me Challenge

Upon entry, we can see that the router doesn't allow connections from the PT-Server-tapdb-backup server, as indicated by the red triangles:

![image](https://github.com/user-attachments/assets/8ea7cb94-8357-4452-af42-7beebd45009c)

## Steps to Solve the Challenge

1. **Connect to the Router**:
   - Use the provided credentials to log in to the router.

2. **Extract the Running Configuration**:
   - Use the command `show running-config` (`sh run`) to extract the current running configuration.

   ![image](https://github.com/user-attachments/assets/cee1f958-81c7-41d5-bca2-5c7c4c84c1b5)

3. **Analyze the Password Encryption**:
   - The password in the configuration is encrypted using Type 7 Cisco encryption.
   - To decrypt the password, use an online tool like [Firewall.cx](https://www.firewall.cx/cisco/cisco-routers/cisco-type7-password-crack.html). After decryption, the password is revealed as `KaliBali`.

   ![image](https://github.com/user-attachments/assets/5af1d395-8ee2-4596-83e2-6dd7fcac0996)

4. **Access Privileged EXEC Mode**:
   - Use the decrypted password `KaliBali` to gain access to privileged EXEC mode.

5. **Inspect IP Interface Configurations**:
   - Use the command `show ip interface brief` to check the status of the interfaces.

   ![image](https://github.com/user-attachments/assets/eec44289-46a0-448f-b87e-7954509bc20d)

6. **Identify the Issue**:
   - The interface `GigabitEthernet0/1` is manually shut down, as seen in the output.

7. **Reactivate the Interface**:
   - Enter global configuration mode using `conf t`.
   - Access the interface configuration using `interface GigabitEthernet0/1`.
   - Use the `no shutdown` command to bring the interface back up.

8. **Verify Connectivity**:
   - After reactivating the interface, the PT-Server-tapdb-backup server is connected to the rest of the network.
   - Confirm this by opening a browser on the PT-Server and accessing the Server-PT at `192.168.1.5`.

9. **Retrieve the Flag**:
   - Once connected, navigate to the Server-PT at `192.168.1.5` to find the flag.

   ![image](https://github.com/user-attachments/assets/2fb66147-a6bd-4a92-badf-4640472f1fcf)

---

This concludes the solution to the "Route Me" challenge. Ensure all changes are saved, and document any additional findings for future reference.

