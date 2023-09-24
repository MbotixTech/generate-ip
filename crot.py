import random
import threading
import re

gash = int(input("How much IP addresses to generate: "))
lmao = int(input("Enter threads: "))

shada = []
humaira = []

def crot(ip):
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    return bool(pattern.match(ip))

def jemboed():
    while len(shada) < gash:
        ip_1 = random.randint(0, 255)
        ip_2 = random.randint(0, 255)
        ip_3 = random.randint(0, 255)
        ip_4 = random.randint(0, 255)
        ip = f"{ip_1}.{ip_2}.{ip_3}.{ip_4}"
        shada.append(ip)

def asukabeh():
    while True:
        if shada:
            ip = shada.pop()
            if crot(ip):
                humaira.append(ip)
                with open("crot.txt", "a") as file:
                    file.write(ip + "\n")
            if len(humaira) >= gash:
                break

generate_thread = threading.Thread(target=jemboed)
validate_thread = threading.Thread(target=asukabeh)
generate_thread.start()
validate_thread.start()
generate_thread.join()
validate_thread.join()
