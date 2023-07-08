import subprocess

""" from prepare_data import prepare_data """
subprocess.call(["./myenv/Scripts/python", "manage.py", "chat_starter"])
subprocess.call(["./myenv/Scripts/python", "manage.py", "runserver"])


