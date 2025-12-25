import json
import sys

def get_count():
    try:
        with open("app.log", 'r') as file:
            content = file.read()
            count_info = content.count('INFO')
            count_warning = content.count('WARNING')
            count_error = content.count('ERROR')
            data = {
                'INFO': count_info,
                'WARNING': count_warning,
                'ERROR': count_error
            }
            log_output(data)
    except FileNotFoundError:
        print("File not found")
        sys.exit()

def log_output(data):
    with open('log_summary.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

get_count()
