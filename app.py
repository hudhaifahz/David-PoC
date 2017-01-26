from flask import Flask, request, render_template, redirect, url_for, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('PoC.html')

@app.route('/motor/<address>', methods=['POST'])
def applySpeed(address):
        speed = request.json['speed']
        print(speed)
        return ''

if __name__ == '__main__':
    app.run(debug=True)
