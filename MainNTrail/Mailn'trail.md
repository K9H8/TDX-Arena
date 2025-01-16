# Mail N Trail CTF Challenge Guide

## Step 1: Check Your IP Address Using the `ipconfig` Command
1. Open Command Prompt.
2. Type `ipconfig` and press **Enter**.
3. Look for the **IPv4 Address** (e.g., `192.168.1.100`). This is your IP address.

---

## Step 2: Add One to Your IP Address and Log into the Mail Server Using Telnet
1. Modify your IP address by adding `1` to the last number.  
   For example, if your IP is `192.168.1.100`, the new IP will be `192.168.1.101`.

2. Enable Telnet if it’s not already installed by typing the following in Command Prompt (Admin):

   ```bash
   dism /online /Enable-Feature /FeatureName:TelnetClient
   ```

3. Open Command Prompt and type:

   ```bash
   telnet 192.168.1.101 110
   ```

   - Replace `192.168.1.101` with the modified IP address you used.

4. Once connected, you should see a greeting from the mail server.

---

## Step 3: Log in Using Username `johnd` and Password `toor`
1. After the greeting from the server, authenticate using the following commands:

   ```bash
   USER johnd
   ```

   - Press **Enter**. The server should respond with `+OK`.

   ```bash
   PASS toor
   ```

   - Press **Enter**. The server should respond with `+OK Password accepted`.

---

## Step 4: Retrieve Messages and Find Splunk Login Credentials
1. After logging in, type the following command to get a list of available messages:

   ```bash
   LIST
   ```

   - Press **Enter**. You should see a list of messages.

2. Retrieve the fourth message by typing:

   ```bash
   RETR 4
   ```

   - Press **Enter**. This will display the content of the fourth message.

3. Inside the fourth message, look for the following credentials:  
   - **Username**: `admin`  
   - **Password**: `CTF_Final!`

4. Open Google Chrome and go to the Splunk login page:

   ```text
   http://192.168.1.101:8000
   ```

   - Replace `192.168.1.101` with the IP address used for Telnet.

5. Log in with the credentials `admin` and `CTF_Final!`.

---

## Step 5: Change the Time Frame and Search for “pastebin”
1. Once logged into Splunk, navigate to **Search & Reporting**.
2. Change the time frame to **All Time** by clicking the time box on the right side of the search bar.
3. In the search bar, enter the following query:

   ```bash
   index=main "pastebin"
   ```

   - Press **Enter** to execute the search.

---

## Step 6: Analyze the Pastebin Search Results and Find the Flag
1. After searching, Splunk will return 56 events. Each event contains a link to `Pastebin.com`.
2. The correct Pastebin link containing the Base64-encoded flag is:

   [https://pastebin.com/raw/0cs1NHvh](https://pastebin.com/raw/0cs1NHvh)

3. Open the Pastebin link in Google Chrome and copy the Base64-encoded string.
4. Decode the Base64 string using an online decoder or a local tool to reveal the flag.

---

**Note**: The final flag is a small sentence in English and not a random string of characters.
```
