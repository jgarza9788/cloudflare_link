

To move files from Google Drive to a local folder in Bash without mounting, you can use the `rclone` tool. Here’s how:

1. **Install rclone**:
   ```bash
   sudo apt install rclone
   ```

2. **Configure rclone**:
   ```bash
   rclone config
   ```
   - Follow the prompts to set up your Google Drive remote.

3. **Move files from Google Drive**:
   ```bash
   rclone move "remote_name:folder_path" /local/destination/
   ```
   Replace `"remote_name:folder_path"` with your configured remote and path in Google Drive, and `/local/destination/` with your local folder path.

### Example:
```bash
rclone move "mydrive:Documents" /home/user/Documents/
```

### Additional Tips:
- Use `rclone ls "remote_name:folder_path"` to list files before moving.
- For more options, check `rclone` documentation: [rclone.org](https://rclone.org/).


---

Here’s how to set up `rclone` for Google Drive:

1. **Open the terminal** and start the configuration process:
   ```bash
   rclone config
   ```

2. **Follow the prompts**:
   - **Type `n`** to create a new remote.
   - **Enter a name** for your remote (e.g., `mydrive`).
   - **Select the storage type**: Type `drive` for Google Drive.
   - **Client ID**: Press Enter to use the default (or enter your own if you have one).
   - **Client Secret**: Press Enter to use the default (or enter your own if you have one).
   - **Scope**: Choose `1` for full access.
   - **Root Folder ID**: Press Enter to use the root directory (or specify a folder ID if needed).
   - **Service Account File**: Press Enter to skip.
   - **Edit advanced config**: Type `n` to skip.
   - **Use auto config**: Type `y` if you're on the same machine with a browser.
   - Follow the link to authorize `rclone` with Google Drive, and paste the authorization code back into the terminal.

3. **Finalize the setup**:
   - **Choose `y`** to confirm the settings.
   - **Type `q`** to quit the configuration.

### Example Commands
Here’s an example session:

```bash
n
mydrive
drive
<Press Enter>
<Press Enter>
1
<Press Enter>
<Press Enter>
n
y
```

### Moving Files
After configuration, use the following command to move files:

```bash
rclone move "mydrive:path/to/files" /local/destination/
```

### Example
```bash
rclone move "mydrive:Documents" /home/user/Documents/
```

This setup should allow you to transfer files from Google Drive to your local system using `rclone`.


```bash
rclone move "mydrive:torrents" /home/jgarza/Downloads
```
