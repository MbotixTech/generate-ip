import random
import threading
import re

num_ips = int(input("How much IP addresses to generate: "))
num_threads = int(input("Enter threads: "))

generated_ips = []
valid_ips = []

def crot(ip):
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    return bool(pattern.match(ip))

def jemboed():
    while len(generated_ips) < num_ips:
        ip_1 = random.randint(0, 255)
        ip_2 = random.randint(0, 255)
        ip_3 = random.randint(0, 255)
        ip_4 = random.randint(0, 255)
        ip = f"{ip_1}.{ip_2}.{ip_3}.{ip_4}"
        generated_ips.append(ip)

def asukabeh():
    while True:
        if generated_ips:
            ip = generated_ips.pop()
            if crot(ip):
                valid_ips.append(ip)
                with open("crot.txt", "a") as file:
                    file.write(ip + "\n")
            if len(valid_ips) >= num_ips:
                break

generate_thread = threading.Thread(target=jemboed)
validate_thread = threading.Thread(target=asukabeh)
generate_thread.start()
validate_thread.start()
generate_thread.join()
validate_thread.join()
