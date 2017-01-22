from flask import Flask, abort, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('PoC.html')

@app.route('/motor/<motorAddress>', methods=['POST'])
def signUpUser(motorAddress):
        slider = request.form['slider1'];
        return render_template('PoC.html');

if __name__ == '__main__':
    app.run(debug=True)
