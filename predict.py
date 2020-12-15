import socket
def menu():
    print("1.IP")
    print("2.URL")

def o1():
    print("")
    var=(input("Enter IP"))
    addr6 = socket.gethostbyaddr(var)  # gives URL
    print(addr6)
def o2():
    print("")
    var = (input("Enter URL"))
    addr1= socket.gethostbyname(var) #gives IP
    print(addr1)

menu()
option=int(input("Enter option"))
if option==1:
    o1()
elif option==2:
    o2()
else:
    print("Invalid")
