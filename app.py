from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('PoC.html')

@app.route('/motor/<controllerAddress>/<motorAddress>', methods=['POST'])
def applySpeed(controllerAddress, motorAddress):
    speed = request.json['speed']
    print(controllerAddress, ' ', motorAddress, ' ', speed)
    return ''

if __name__ == '__main__':
    app.run(debug=True)
