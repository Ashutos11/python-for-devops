import json

def read_logs():
    file_name = "D:/github/python-for-devops/day-09/devops-utilities-api/services/app.log"
    try:
        with open(file_name, "r") as file:
            return file.readlines()
    except:
        raise FileNotFoundError
    
def analyze_logs():
    log_count = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    lines = read_logs()

    for line in lines:
        if "INFO" in line:
            log_count.update({"INFO": log_count["INFO"]+1})
        elif "WARNING" in line:
            log_count.update({"WARNING": log_count["WARNING"]+1})
        elif "ERROR" in line:
            log_count.update({"ERROR": log_count["ERROR"]+1})
        else:
            pass
    
    return log_count
