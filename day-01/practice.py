import psutil

# input

cpu = int(input())
mem = int(input())
desk = int(input())

# sytem value

rcpu = psutil.cpu_percent(interval=1)
rmem = psutil.virtual_memory().percent
rdesk = psutil.disk_usage("/").percent

# output

if cpu > rcpu:
    print("CPU HIGH", "-----USING", rcpu, "%")
else:
    print("CPU OK", "-----USING", rcpu, "%")
if mem > rmem:
    print("MEMORY HIGH", "-----USING", rmem, "%")
else:
    print("MEMORY OK", "-----USING", rmem, "%")
if desk > rdesk:
    print("DISK HIGH", "-----USING", rdesk, "%")
else:
    print("DISK OK", "-----USING", rdesk, "%")
