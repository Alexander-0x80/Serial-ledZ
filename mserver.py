import bottle
import serial

SERIAL_PORT = '/dev/ttyUSB0'

app = bottle.Bottle()

try:
    serial_port = serial.Serial(SERIAL_PORT,9600)
except serial.SerialException:
    exit("Cannot open serial port")


@app.post("/test")
def test():
    data = bottle.request.json
    if data is not None:
        pixels = data["pixels"]
        for p in pixels:
            serial_port.write(chr(p))
        #serial_port.write("*")
    else:
        print "DATA ERROR"


@app.route('/App/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='App')

app.run(host="localhost",port=80,debug=True)
