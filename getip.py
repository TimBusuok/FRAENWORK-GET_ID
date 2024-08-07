from pyfiglet import figlet_format
import socket
import sys


def get_id(target_host):
    try:
        ip = socket.gethostbyname(target_host)
        return ip
    except socket.gaierror:
        print("Invalid IP\nPlease check your Hostname!!")
        return None  # Возвращаем None, чтобы знать, что IP не найден


print("  ____ _____ _____   ___ ____")
print(" / ___| ____|_   _| |_ _|  _ \ ")
print("| |  _|  _|   | |    | || |_) |")
print("| |_| | |___  | |    | ||  __/")
print(" \____|_____| |_|   |___|_| ")

print("If you want help then write help")

print("                                                       ")
print("")
print("")

while True:
    ans = str(input("Enter your HOSTNAME(Example:<URL>.(com,ru and etc)):"))
    if ans == "exit":
        print("GoodBye")
        break  # Выход из цикла, если пользователь ввел "exit"
    if ans == "help":
        print("if you want exit them write in console - exit\nFunction in development")
    else:
        IP = get_id(ans)
        if IP:
            print("{} ==> {}".format(ans, IP))
        else:
            print("IP not found.")
