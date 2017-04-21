from picamera import PiCamera
import SimpleHTTPServer
import SocketServer
import io

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

socket = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
socket.serve_forever()


try:
 while True:
  conn = socket.accept()
  my_stream = BytesIO()
  camera = PiCamera()
  camera.start_preview()
  camera.capture(my_stream, 'jpeg') 
  conn.sendall(my_stream)
  conn.close()
finally:
 socket.close()
