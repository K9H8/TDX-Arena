#Challenge 

Here’s a step-by-step breakdown of how I discovered the credentials and gained access:

### 1. **Initial Exploration**
   I started by exploring the system files and logs using basic enumeration:
   - I checked various directories, like `/var/log`, to find relevant information related to system activity.
   - I was looking for any traces of login credentials or other sensitive information.

### 2. **Checking the `.todos.json` File:

   I executed a search for the term "password" within my home directory:
   
   ```
find /home/thomas -type f -exec grep -i "password" {} +
   ```

   This led to discovering an entry in the `.todos.json` file that referenced Nathan and a "Password Update" task:
   - **Task 4**: "Check password and login for @Nathan about +Password Update."
   - **Task 5**: "Delete mail from @Nathan about +Password Update."

   This gave me a clue that there might be sensitive information related to passwords in the system, possibly in an email or another file.

#### `-exec grep -i "password" {} +`

- **`-exec`**: The `-exec` option allows you to execute a command (in this case, `grep`) on each file that `find` locates.
- **`grep -i "password"`**: This part runs the `grep` command on the files found by `find`. `grep` searches for the string "password" inside the files:
    - **`-i`**: This makes the search case-insensitive, so it will match "password" regardless of whether it's in uppercase or lowercase (e.g., "PASSWORD," "Password").
- **`{}`**: The `{}` is a placeholder that represents each file found by `find`. For every file found, `grep` is executed on that file.
- **`+`**: The `+` at the end is used to group multiple files together when passing them to `grep`, making the command more efficient by minimizing the number of times `grep` is executed.
- 
### 3. **Searching for Deleted Emails**

   I found a file called `mail.htm` in the trash directory (`/home/thomas/.local/share/Trash/files/`), which suggested there could be valuable information about Nathan’s password update:
   
   ```
   cat /home/thomas/.local/share/Trash/files/mail.htm
   ```

### 4. **Extracting Credentials from the Email**

   The content of `mail.htm` contained an email from Nathan, asking someone to check if the new password worked. The email included:
   - **Login**: `admin`
   - **Password**: `vYuzpN9MTHdxWw5a`

   This gave me both the login credentials and a request to verify if they worked.

### 5. **Logging into the System**

   Using the credentials I found in the email, I successfully logged into the system with:
   - **Username**: `admin`
   - **Password**: `vYuzpN9MTHdxWw5a`

### 6. **Gaining Access**
   Once logged in, I confirmed I had gained administrative access to the system, fulfilling the objective.

---

### Summary of Key Steps:

1. **File Search for Sensitive Information**: Using `grep` to search for password-related entries in files.
2. **Analysis of `.todos.json`**: Finding clues in task management data.
3. **Inspecting Trash Files**: Looking through `mail.htm` for references to login credentials.
4. **Successful Login**: Using the credentials from Nathan's email to log into the system.

