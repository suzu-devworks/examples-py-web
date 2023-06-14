from logging import getLogger
from typing import Any, TypeVar

import cv2

T = TypeVar("T", covariant=True)

logger = getLogger(__name__)


class VideoCamera(object):
    video: Any

    def __init__(self, url: str):
        # self.video = cv2.VideoCapture(0)
        self.video = cv2.VideoCapture(url)
        if self.video.isOpened():
            logger.info(f"Open! {url}")

        pass

    def __del__(self):
        self.video.release()
        pass

    def get_frame(self):
        success, image = self.video.read()

        ret, jpeg = cv2.imencode(".jpg", image)
        return jpeg.tobytes()
