# Scripts for use with Streamer.bot

## streamerbot-code-backup.py

- Edit the `actions_json_path` variable to match your file location. (_This means you can use the script to extract the code from an old backup file as well as your current configuration._)
- The script creates a backup directory in the location of the script file, using the current date and time.
- All scripts are extracted from the `actions.json` file and put in this directory named by the action name and a number.
- A backup of your full `actions.json` file is also saved. If you don't want this, comment the two marked lines in the script (31 and 32).

