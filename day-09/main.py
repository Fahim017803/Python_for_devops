import json
from fastapi import FastAPI

app = FastAPI()

def analysis_log():
    info = 0
    warning = 0
    error = 0

    with open("input.txt", "r") as s:
        for line in s:
            info += line.count("INFO")
            warning += line.count("WARNING")
            error += line.count("ERROR")

    return {"INFO": info, "WARNING": warning, "ERROR": error}


@app.get("/fahim")
def fahim():
    
    result=analysis_log()
    with open("output.json", "w") as f:
        json.dump(result, f, indent=20) #in production, writing file is a risk of overwrite in same file.
        
    return result
