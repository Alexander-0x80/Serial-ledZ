import bottle
import serial
import sys

if len(sys.argv) < 2:
    exit("No port is given!")

SERIAL_PORT = sys.argv[1]
DEBUG = False

app = bottle.Bottle()

try:
    serial_port = serial.Serial(SERIAL_PORT, 9600)
except serial.SerialException:
    exit("Cannot open serial port")


@app.route("/")
def main():
    return bottle.static_file("index.html", root="App")


@app.post("/matrix")
def test():
    data = bottle.request.json
    if data is not None:
        pixels = data["pixels"]
        serial_port.write("".join([chr(p) for p in pixels]))
    else:
        print "DATA ERROR"


@app.route('/App/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='App')

app.run(host="0.0.0.0", port=8080, debug=DEBUG)
