# Stream-Camera-over-HTTP
For Streaming OpenCV camera and recieving on another machine via HTTP using FLASK and Python.

## Pre-requisites:
Flask, OpenCV

# Multiple Camera Streaming (multiplecamera folder)
Contains code streaming 4 cameras over HTTP at once. 
Currently code only works with 4 cameras, no more or less. 
Each camera ID has to be found beforehand and edited in the code. 
Unplugging/disabling camera during the code running will cause code to crash
Framerate of stream depends on resolution of each frame set and USB bandwidth. Recommended for highest framerate of approx. 15fps is 640X320 per camera creating a 1280X720 video feed when all 4 cameras are stitched together.

Code here is also used in my other repo: https://github.com/ProjectHydroTech/Pynq-Frontend

## How it works:
Camera frames from each of the 4 cameras are captured using OpenCV while multithreaded. Each frame is then stitched together as numpy array into 1 singular frame which is then passed on to the Flask app to be shown as a HTML stream

## How To Use:
Navigate to directory and run
```
set FLASK_APP=camera.py
flask run
```
Then in any web browser navigate to HOSTIP:5000 to view stream
5000 is the port I set in the code, feel free to change as per your usage.

# Single Camera Streaming (singlecamerafolder)
Contains code streaming a single camera over HTTP AND photo taking at regular intervals
Able to autodetect camera ID (-1 to 3) and start stream based on the opened ID
Use for AI data collection of images. In my case, tracking growth and different lighting conditions for vegetables on a hydroponics rack.
Images are saved in the format opencv_frame_{time taken}.jpg under a /imgs folder u have to create in the same directory.

## Settings:
Currently code auto flips image and saves it upside down my webcam is mounted upside down.
```
flip = cv2.flip(frame, flipCode = -1) # flips webcam feed 180
```
Remove this line 
```
ret, buffer = cv2.imencode('.jpg', flip)
```
Change flip to frame to revert changes

You can set the photo taking interval with 
```
if time.time() - start_time >= 300: #in seconds #5mins
```

## How to Use:
Navigate to /singlecamera directory and run
```
set FLASK_APP=app.py
flask run
```
Then in any web browser navigate to HOSTIP:5000 to view stream
5000 is the port I set in the code, feel free to change as per your usage.



