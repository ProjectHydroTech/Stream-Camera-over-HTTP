import cv2
from base_camera import BaseCamera
import numpy as np


class Camera(BaseCamera):
    video_source1 = 0
    video_source2 = 2

    @staticmethod
    def set_video_source(sources):
        Camera.video_source1 = sources[0]
        Camera.video_source2 = sources[1]

    @staticmethod
    def frames():
        camera1 = cv2.VideoCapture(Camera.video_source1)
        camera2 = cv2.VideoCapture(Camera.video_source2)
        if not (camera1.isOpened() or camera2.isOpened()):
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img1 = camera1.read()
            _, img2 = camera2.read()
            img1 = cv2.resize(img1, (704, 396))
            img2 = cv2.resize(img2, (704, 396))
            img = np.hstack((img1, img2))

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
