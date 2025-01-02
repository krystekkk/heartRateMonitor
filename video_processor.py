import numpy as np
import cv2


class VideoProcessor:
    def __init__(self, video_path):
        self.video_path = video_path
        self.means = []  # List of mean pixel values

    def process_video(self):
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            raise IOError(f"Unable to open video: {self.video_path}")

        while(cap.isOpened()):
            ret, frame = cap.read()  # read a single frame
            if not ret:
                break

            (height, width, channels) = frame.shape
            crop_frame = frame[int(height / 2 - 150):int(height / 2 + 150), int(width / 2 - 150):int(width / 2 + 150), 0]  # 300x300
            mean = np.mean(crop_frame, dtype=np.float64)
            self.means.append(mean)

        cap.release()
        cv2.destroyAllWindows()
        return self.means
