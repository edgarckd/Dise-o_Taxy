from socketserver import BaseRequestHandler, UDPServer
import time
import mysql.connector
cnn = mysql.connector.connect(host="database-1.cenhvg7ksmup.us-east-1.rds.amazonaws.com", user = "admin", passwd = "HanbookRadar97", database="ubicacion")


class GestorSolicitudesHora(BaseRequestHandler):
    def handle(self):
        print('se ah recibido una conexion desde {}' .format(self.client_address))
        mensaje, sock = self.request
        respuesta = time.ctime()
        sock.sendto(respuesta.encode('ascii'),self.client_address)
        
        mensaje=str(mensaje)
        mensaje=mensaje[2:7]
        cordenada = mensaje
        hora = respuesta
        cur = cnn.cursor()
        cur.execute("INSERT INTO gru (cordenada, hora) VALUES ('{}','{}')" .format(hora, cordenada))
        cnn.commit()
        cur.close()

        

        
        

if __name__ == '__main__':
    servidor = UDPServer(('',37777), GestorSolicitudesHora)
    print('se ah iniciado el servidor')
    servidor.serve_forever()
