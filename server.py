from socket import *
import csv
import json

serverPort=6500
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
    
while True:
    connectionSocket, addr = serverSocket.accept()
     
    sentence = connectionSocket.recv(1024).decode()
    #print(addr)
    #print(connectionSocket)
    print(sentence)
    ip=addr[0]
    portNumber=addr[1]
    url = sentence.split()[1] 
    if url == '/' or url.endswith("index.html"):
        f = open("C:\\Users\\User\\Desktop\\Network\\Project\\Question3\\main.html")
        file = f.read()
        f.close()
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(file.encode()) 
    if  url.endswith("second.html"):
        f = open("C:\\Users\\User\\Desktop\\Network\\Project\\Question3\\second.html")
        file = f.read()
        f.close()
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(file.encode()) 

    elif url.endswith(".css"):
        f = open("C:\\Users\\User\\Desktop\\Network\\Project\\Question3\\Styles.css")
        ff = f.read()
        f.close()

        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/css \r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(ff.encode())    

    elif url.endswith(".png"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png \r\n".encode())
        connectionSocket.send("\r\n".encode())

        image = open("C:\\Users\\User\\Desktop\\Network\\Project\\Question3\\tea.png",'rb')
        png = image.read()
        image.close()
        connectionSocket.send(png)


    elif url.endswith(".jpg"):
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpg \r\n".encode())
        connectionSocket.send("\r\n".encode())
        image = open("C:\\Users\\User\\Desktop\\Network\\Project\\Question3\\keyboard.jpg",'rb')
        jpg = image.read()
        image.close()
        connectionSocket.send(jpg)     


    elif url.endswith("SortByPrice"):
        items= []
        with open("C:\\Users\\User\\Desktop\\Network\\Project\\Question3\\list.csv",'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                items.append(row)

        for i in range(1,len(items)):
            for j in range(0,len(items)-1):
                if int(items[j][1]) > int(items[j+1][1]):
                    tempName = items[j][0]
                    tempPrice = items[j][1]
                    items[j][0] = items[j+1][0]
                    items[j][1] = items[j+1][1]
                    items[j+1][0] = tempName
                    items[j+1][1]=tempPrice

        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/plain \r\n".encode())
        connectionSocket.send("\r\n".encode())

        for i in range(0,len(items)):
            for j in range(0,len(items[i])):
                connectionSocket.send(items[i][j].encode() +"\t\t".encode())
                if j == 0 :
                    connectionSocket.send(":".encode())
            connectionSocket.send("\n".encode())
       

    elif url.endswith("SortByName"):
        items= []
        with open("C:\\Users\\User\\Desktop\\Network\\Project\\Question3\\list.csv",'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                items.append(row)
        for i in range(1,len(items)):
            for j in range(0,len(items)-1):
                if items[j][0] > items[j+1][0]:
                    tempName = items[j][0]
                    tempPrice = items[j][1]
                    items[j][0] = items[j+1][0]
                    items[j][1] = items[j+1][1]
                    items[j+1][0] = tempName
                    items[j+1][1]=tempPrice

                    
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/plain \r\n".encode())
        connectionSocket.send("\r\n".encode())

        for i in range(0,len(items)):
            for j in range(0,len(items[i])):
                connectionSocket.send(items[i][j].encode() +"\t\t".encode())
                if j == 0 :
                    connectionSocket.send(":".encode())
            connectionSocket.send("\n".encode())

    else:
        f = open("C:\\Users\\User\\Desktop\\Network\\Project\\Question3\\error.html")
        file = f.read().format(ip=ip,port=portNumber)
        f.close()

        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(file.encode()) 


    connectionSocket.close()  