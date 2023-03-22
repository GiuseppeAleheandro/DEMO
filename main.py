import subprocess
import os
import importlib

import time
os.system("clear")
print("Checking All Requirements ...")
time.sleep(3)
with open('requirements.txt', 'r') as f:
    modules = f.read()
# Try to import the module
try:
    os.system('clear')
    importlib.import_module(modules)
    import cv2
    import numpy as np
    from flask import Flask, render_template, Response
    camera = cv2.VideoCapture(0)

    def gen_frames():
        while True:
            success, frame = camera.read()
            if not success:
                break
            else:
                # Convert the frame to a byte array
                ret, buffer = cv2.imencode('.jpg', frame)
                frame_bytes = buffer.tobytes()

                # Yield the byte array as an HTTP response
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/video_feed')
    def video_feed():
        return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

    if __name__ == '__main__':
        app.run(debug=True)

    
except ImportError:
    os.system('clear')
    print("Err: Please Run pip3 install -r requirements.txt")
    exit()

app = Flask(__name__)