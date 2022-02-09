import cv2
from base_camera import BaseCamera
import numpy as np


class camera(BaseCamera):
    video_source1 = 0
    video_source2 = 2
    video_source3 = 4
    video_source4 = 6

    @staticmethod
    def set_video_source(sources):
        print(sources)
        camera.video_source1 = sources[0]
        camera.video_source2 = sources[1]
        camera.video_source3 = sources[2]
        camera.video_source4 = sources[3]
        
    @staticmethod
    def frames():
        
        camera1 = cv2.VideoCapture(camera.video_source1)
        camera1.set(3, 800)
        camera1.set(4, 800)

            
        camera2 = cv2.VideoCapture(camera.video_source2)
        camera2.set(3, 800)
        camera2.set(4, 800)

            
        camera3 = cv2.VideoCapture(camera.video_source3)
        camera3.set(3, 800)
        camera3.set(4, 800)

            
        camera4 = cv2.VideoCapture(camera.video_source4)
        camera4.set(3, 800)
        camera4.set(4, 800)
        
        if not (camera1.isOpened() or camera2.isOpened() or camera3.isOpened() or camera4.isOpened()):
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img1 = camera1.read()
            img1 = cv2.resize(img1, (640, 320))
            _, img2 = camera2.read()
            img2 = cv2.resize(img2, (640, 320))
            _, img3 = camera3.read()
            img3 = cv2.resize(img3, (640, 320))
            _, img4 = camera4.read()
            img4 = cv2.resize(img4, (640, 320))

            imgh1 = np.hstack((img1, img2))
            imgh2 = np.hstack((img3, img4))
            imgv = np.vstack((imgh1, imgh2))

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
