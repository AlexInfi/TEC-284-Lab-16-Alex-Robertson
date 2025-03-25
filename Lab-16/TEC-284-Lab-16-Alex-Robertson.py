from flask import Flask, render_template
from gpiozero import LED

app = Flask(__name__)
led1 = LED(18)
led2 = LED(23)
led3 = LED(24)

@app.route('/')
def index():
    return render_template('HTML Code.html')

@app.route('/toggle/<action>')
def LEDControl(action):
    if action == '1on':
        led1.on()
        return 'LED 1 Turned On'
    elif action == '1off':
        led1.off()
        return 'LED 1 Turned Off'
    
    if action == '2on':
        led2.on()
        return 'LED 2 Turned On'
    elif action == '2off':
        led2.off()
        return 'LED 2 Turned Off'
    
    if action == '3on':
        led3.on()
        return 'LED 3 Turned On'
    elif action == '3off':
        led3.off()
        return 'LED 3 Turned Off'

if __name__ == '__main__':
    app.run(host='192.168.1.11', port=8080)