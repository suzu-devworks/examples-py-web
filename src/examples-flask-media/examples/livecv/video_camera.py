import threading
import time
from logging import getLogger
from typing import Any, TypeVar

import cv2

T = TypeVar("T", covariant=True)

logger = getLogger(__name__)


class VideoCamera(object):
    source: str
    framerate: int
    video: Any
    running: bool
    thread: threading.Thread
    has_image: Any
    image: Any

    def __init__(self, source: str, framerate: int = 30):
        self.source = source
        self.framerate = framerate
        self.has_image = False
        self.running = False

    def __del__(self) -> None:
        self.stop()
        if self.video is not None:
            self.video.release()

    def start(self) -> None:
        if self.running:
            return

        self.video = cv2.VideoCapture(self.source)
        if self.video.isOpened():
            logger.info(f"Open! {self.source}")

        self.thread = threading.Thread(target=self.read_frame)
        self.thread.start()

        self.running = True
        logger.info("started.")

    def stop(self) -> None:
        if self.thread is not None:
            self.thread.join()
        self.running = False
        logger.info("stoped.")

    def read_frame(self) -> None:
        while self.running:
            success, image = self.video.read()
            if not success:
                logger.warn("read end.")
                break

            self.image = image
            self.has_image = success

            # time.sleep(.1)  # 0.1s to use less CPU
            time.sleep(1 / self.framerate)

    def get_frame(self) -> Any:
        if (not self.running) or (not self.has_image):
            return None

        image = self.image
        ret, jpeg = cv2.imencode(".jpg", image)
        return jpeg.tobytes()

    def get_gray_frame(self) -> Any:
        if (not self.running) or (not self.has_image):
            return None

        image = self.image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        ret, jpeg = cv2.imencode(".jpg", gray)
        return jpeg.tobytes()
