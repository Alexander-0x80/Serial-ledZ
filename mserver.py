import bottle
import serial

app = bottle.Bottle()

try:
    serial_port = serial.Serial('/dev/ttyUSB0',9600)
except serial.SerialException:
    exit("Cannot open serial port")

@app.post("/test")
def test():
    data = bottle.request.POST.get("pixels")
    if data is not None:
       serial_port.write(data)

@app.route('/App/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='App')

app.run(host="localhost",port=80)
