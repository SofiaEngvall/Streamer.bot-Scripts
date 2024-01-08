# streamerbot-code-backup
# by Sofia Engvall
# 2024-01-08

import os
import json
import base64
from datetime import datetime

# Put your streamer.bot configurations path here
actions_json_path = "C:\\VIDEO\\Streamer.bot\\data\\actions.json"

# The backup is but in a subdirectory of where the script is maked with date and time of the backup
timestamp = datetime.now().strftime("-%Y%m%d-%H%M%S")
backup_files_path = os.path.join(os.path.dirname(__file__), "backup"+timestamp)

if not os.path.exists(actions_json_path):
    print("The path to streamer.bots actions.json is incorrect.\n")
    exit()

with open(actions_json_path, "r") as sb_file:
    file_text = sb_file.read()

file_json = json.loads(file_text)
# print(f"\njson in:\n{file_json}\n\n")

if not os.path.exists(backup_files_path):
    os.makedirs(backup_files_path)

# Backing up the actions.json too. Comment these if you don't want to
with open(os.path.join(backup_files_path, "actions.json"), "w") as sb_file:
    sb_file.write(file_text)

# Go through all the actions
for action in file_json['actions']:
    count = 0

    # Go through all sub actions
    for sub_action in action['actions']:

        # If the sub action type is Execute Code
        if sub_action['type'] == 99999:
            count += 1

            #  The code is saved in the json in base64 format so it needs to be decoded
            code_base64 = sub_action['byteCode']
            code_text = base64.b64decode(code_base64).decode(
                'utf-8').replace("\r", "")

            # Saving all the code bits to files names by the action and number
            with open(os.path.join(backup_files_path, action['name']+" "+str(count)+".cs"), 'w') as cs_file:
                cs_file.write(code_text)
