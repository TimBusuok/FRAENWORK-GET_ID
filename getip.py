from pyfiglet import figlet_format
import socket
import sys

def get_id(target_host):
    try:
        ip = socket.gethostbyname(target_host)
        return ip
    except socket.gaierror:
        print("Invalid IP\nPlease check your Hostname!!")
        return None # Возвращаем None, чтобы знать, что IP не найден

print(figlet_format("GET IP", font="isometric3"))
print("If you want help then write help")

while True:
    ans = str(input("Enter your HOSTNAME(Example:<URL>.(com,ru and etc)):"))
    if ans == "exit":
        break # Выход из цикла, если пользователь ввел "exit"
    if ans == "help":
        print("if you want exit them write in console - exit\nFunction in development")
    else:
        IP = get_id(ans)
        if IP:
            print("{} ==> {}".format(ans, IP))
        else:
            print("IP not found.")