from flask import Flask, request, render_template, url_for
import serial

port="/dev/serial0"
saberTooth = serial.Serial(port, 9600)
Ramping = 16
ForwardMotor1 = 0
BackwardsMotor1 = 1
ForwardMotor2 = 4
BackwardsMotor2 = 5

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('PoC.html')

@app.route('/motor/<int:controllerAddress>/<int:motorAddress>', methods=['POST'])
def applySpeed(controllerAddress, motorAddress):
    speed = request.json['speed']
    print(controllerAddress, ' ', motorAddress, ' ', speed)
    if (motorAddress == 1):
        if (speed >= 0):
            doCommand(controllerAddress, ForwardMotor1, speed)
        else:
            doCommand(controllerAddress, BackwardsMotor1, abs(speed))
    elif (motorAddress == 2):
        if (speed >= 0):
            doCommand(controllerAddress, ForwardMotor2, speed)
        else:
            doCommand(controllerAddress, BackwardsMotor2, abs(speed))
        
    return ''

def doCommand(controllerAddress, command, parameter):
    global saberTooth
    commandElements = [controllerAddress, command, parameter, (controllerAddress + command + parameter)&127]
    saberTooth.write(bytearray(commandElements))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
