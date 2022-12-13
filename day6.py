with open("day6input.txt", "r") as f:
    buffer = f.readline()

for i in range(len(buffer)):
    next4 = buffer[i:i+4]
    if len(set(next4)) == len(next4):
        print(f"First start of packet marker at {i+4}")
        break

for i in range(len(buffer)):
    next14 = buffer[i:i+14]
    if len(set(next14)) == len(next14):
        print(f"First start of message marker at {i + 14}")
        break

