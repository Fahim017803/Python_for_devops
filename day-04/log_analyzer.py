info = 0
warning = 0
error = 0

try:
    with open("input.txt", "r") as s:
        for line in s:
            info+=line.count("INFO")
            warning+=line.count("WARNING")
            error+=line.count("ERROR")
    
except:
    print("file not found")
    exit()

print(info, warning, error)

with open("output.txt", "w") as s:
     s.write(f"info found : {info}\n")
     s.write(f"warning found : {warning}\n")
     s.write(f"error found : {error}\n")