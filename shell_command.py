import os
from flask import send_file, jsonify

def command() :
    shell_command = "./make_env.sh"
    os.system(shell_command)

def check_string_in_file():
    try:
        with open("/home/m0nd2y/SearchVuln/finish", 'r') as file:
            for line in file:
                if "done" in line:
                    return True
        return False
    except IOError:
        return False