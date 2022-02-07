from flask import Flask, render_template, Response
import numpy
import cv2
import os
import time
from IPython.display import display
from PIL import Image

app = Flask(__name__)

global start_time

def gen_frames(index):  # generate frame by frame from camera
    camera = cv2.VideoCapture(index)
    camera.set(3, 1280)
    camera.set(4, 720)
    start_time = time.time()
    print(start_time)
    print(time.cime(start_time))
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            camera.release()
            break
        else:
            frame_set = []
            flip = cv2.flip(frame, flipCode = -1) # flips webcam feed 180
            ret, buffer = cv2.imencode('.jpg', flip)
            buffered = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + buffered + b'\r\n')  # concat frame one by one and show result
            if time.time() - start_time >= 300: #in seconds #5mins
                print(time.time() - start_time)
                local_time = time.ctime(start_time)
                img_name = "imgs/opencv_frame_{}.jpg".format(local_time)
                cv2.imwrite(img_name, flip)
                print("{} written!".format(local_time))
                #display(Image.open(img_name)) # shows image within jupyter ( crashes after a while, use for testing only )
                start_time = time.time() #resets timer 

def testDevice():
    index = 0
    for index in range(-1, 3):  #checks camera -1 through 3
        camera = cv2.VideoCapture(index)
        camera.set(3, 1280)
        camera.set(4, 720)
        print('opening camera {}'.format(index))
        break
        if camera is None or not camera.isOpened():
            print('Warning: unable to open camera: ', index)
            print('Changing to camera: ', index)
    camera.release()
    if index == 3:
        print('Unable to find camera')
    else:
        return gen_frames(index)
        

@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(testDevice(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5000") #0.0.0.0 allows for ip to be broadcasted as the ip of the host board at port 5000