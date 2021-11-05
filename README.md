# Stream-Camera-over-HTTP
For Streaming OpenCV camera and recieving on another machine via HTTP

Copy Video Stream Out to host board, in this case an ULTRA96 but anything that supports jupyter notebook is also appropriate and run run.ipynb in a jupyter notebook to activate
In app.py:
- Make sure camera = cv2.VideoCapture(0) is set to your correct webcam, in this case 0
- You can change the port number to your liking, in this case port 5000
- You can also visit the broadcasted webpage at ipaddress:5000
In run.ipynb:
- Make sure OpenCV and Flask is installed and working

Copy Video Stream In to remote machine (e.g. Laptop ) and run run.ipnyb to recieve the Video stream
