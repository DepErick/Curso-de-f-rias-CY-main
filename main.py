from flask import Flask, render_template, request
import serial
import time

# Configure a porta serial do Arduino (ajuste a COM se necessário)
arduino = serial.Serial('COM8', 9600)  # Ex: 'COM3' no Windows ou '/dev/ttyUSB0' no Linux
time.sleep(2)  # Tempo para inicializar

app = Flask(__name__)

estado_led = False

@app.route('/')
def index():
    return render_template('index.html', estado=estado_led)

@app.route('/ligar')
def ligar():
    global estado_led
    arduino.write(b'1')
    estado_led = True
    return render_template('index.html', estado=estado_led)

@app.route('/desligar')
def desligar():
    global estado_led
    arduino.write(b'0')
    estado_led = False
    return render_template('index.html', estado=estado_led)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
