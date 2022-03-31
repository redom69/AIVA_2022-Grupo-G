import detect_client_in_frame
import torch
import numpy as np
import cv2
from time import time

class VideoDetection:

    def __init__(self,video, out_file):
        """
        Initializes the class with youtube url and output file.
        :param url: Has to be as youtube URL,on which prediction is made.
        :param out_file: A valid output file name.
        """
        self._video = video
        self.model = self.load_model()
        self.out_file = out_file
        self.bounding_box = []
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

    def get_video(self):
        """
        Creates a new video streaming object to extract video frame by frame to make prediction on.
        :return: opencv2 video capture object, with lowest quality frame available for video.
        """
        return cv2.VideoCapture(self._video)

    def load_model(self):
        """
        Loads Yolo5 model from pytorch hub.
        :return: Trained Pytorch model.
        """
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

        return model


    def __call__(self):
        """
        This function is called when class is executed, it runs the loop to read the video frame by frame,
        and write the output into a new file.
        :return: void
        """
        player = self.get_video()
        assert player.isOpened()
        x_shape = int(player.get(cv2.CAP_PROP_FRAME_WIDTH))
        y_shape = int(player.get(cv2.CAP_PROP_FRAME_HEIGHT))
        four_cc = cv2.VideoWriter_fourcc(*"MJPG")
        out = cv2.VideoWriter(self.out_file, four_cc, 20, (x_shape, y_shape))
        while True:
            start_time = time()
            ret, frame = player.read()
            if not ret:
                break
            fd = detect_client_in_frame.frameDetection(frame)
            results = detect_client_in_frame.frameDetection.score_frame(fd,frame,self.model)
            frame = detect_client_in_frame.frameDetection.plot_boxes(fd,results, frame)
            end_time = time()
            print(fd.bounding_box)
            fps = 1 / np.round(end_time - start_time, 3)
            print(f"Frames Per Second : {fps}")
            out.write(frame)


