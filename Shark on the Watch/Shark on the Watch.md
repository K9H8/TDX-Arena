# Solving the Wireshark Challenge: "Shark on the Watch"

This step-by-step guide will help you solve the Wireshark challenge titled **"Shark on the Watch."**

## Step 1: Apply an FTP Filter
1. Use the filter to narrow down the packets related to FTP and FTP data transfer.
   ```
   ftp || ftp-data
   ```
2. Analyze the filtered packets to identify suspicious activity.

   - Notice that Boris has attempted a **brute-force attack** to gain access to an account.
   - Inspect the details in the packets to confirm the brute-force activity.
   - The correct password was "password123".

   ![image](https://github.com/user-attachments/assets/9d3808a3-e55d-4b06-86a8-ebf07d5cebc0)


## Step 2: Focus on FTP Data Packets
1. Adjust the filter to only show FTP data packets:
   ```
   ftp-data
   ```
2. Look through the packets in this filtered view.

   - Identify a **specific packet** that contains the CTF flag.
  

## Step 4: Extract the Flag
1. Inspect the content of the relevant packet (right-click > "Follow" > "TCP Stream" or "FTP-DATA Stream").
2. Search for the flag within the data stream.
   - The flag is typically in a recognizable format (e.g., `flag{...}`).

![image](https://github.com/user-attachments/assets/b2965869-f8cd-453b-903a-dd22d78e42a3)
