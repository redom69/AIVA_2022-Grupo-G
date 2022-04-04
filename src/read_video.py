import cv2
import torch
import src.detect_client_in_frame as detect_client_in_frame
from collections import deque
from tqdm import tqdm


class VideoDetection:

    def __init__(self, video, out_file):
        """
        Initializes the class with youtube url and output file.
        :param url: Has to be as youtube URL,on which prediction is made.
        :param out_file: A valid output file name.
        """
        self._video = video
        self.model = self.load_model()
        self.out_file = out_file
        self.test_frame = []
        self.bounding_box_test = []
        self.videoIsClosed = False
        self.entran = 0
        self.salen = 0
        self.esperan = 0

    def get_video(self):
        """
        Creates a new video streaming object to extract video frame by frame to make prediction on.
        :return: opencv2 video capture object, with lowest quality frame available for video.
        """
        return cv2.VideoCapture(self._video)

    @staticmethod
    def load_model():
        """
        Loads Yolo5 model from pytorch hub.
        :return: Trained Pytorch model.
        """
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

        return model

    def get_test_frame(self):
        """
        Function for unitary tests
        :return:  Test frame for unitary test
        """
        return self.test_frame

    def count_frames_manually(self):
        frame_count = 0
        video = self.get_video()
        # Iteraremos sobre cada "frame" en el video, incrementando el conteo.
        while True:
            frame_was_read, _ = video.read()

            # Dejamos de iterar cuando ya no haya más cuadros en el video.
            if not frame_was_read:
                return frame_count

            frame_count += 1

    def __call__(self):
        """
        This function is called when class is executed, it runs the loop to read the video frame by frame,
        and write the output into a new file.
        :return: void
        """
        bbx = None
        c_entran = []
        c_l1 = []
        c_l2 = []
        c_paran = []
        player = self.get_video()
        assert player.isOpened()
        x_shape = int(player.get(cv2.CAP_PROP_FRAME_WIDTH))
        y_shape = int(player.get(cv2.CAP_PROP_FRAME_HEIGHT))
        four_cc = cv2.VideoWriter_fourcc(*"MJPG")
        out = cv2.VideoWriter(self.out_file, four_cc, 20, (x_shape, y_shape))
        pos_y_ant = []
        x_anteriores = deque([], maxlen=10)
        pos = 0
        progress = tqdm(total=self.count_frames_manually(), position=0, desc="Executing...")
        while True:
            ret, frame = player.read()
            if not ret:
                break
            fd = detect_client_in_frame.FrameDetection(frame)
            results = fd.score_frame(frame, self.model)
            frameout, pos_y, pos_x = fd.plot_boxes(results, frame)
            x_anteriores.appendleft(pos_x)
            ent = fd.entran(pos_y, pos_y_ant)
            l1, l2 = fd.pasan(pos_x)
            sp, pos = fd.se_paran(pos_x, x_anteriores, pos)
            pos_y_ant = pos_y
            c_entran.append(ent)
            c_l1.append(l1)
            c_l2.append(l2)
            c_paran.append(sp)
            if len(fd.bounding_box) > 0:
                self.test_frame = frame
                bbx = fd.test_bounding_box(results, frame)
            out.write(frameout)
            self.bounding_box_test = bbx
            self.videoIsClosed = True
            self.entran = sum(c_entran)
            self.salen = min(sum(c_l1), sum(c_l2))
            self.esperan = sum(c_paran)
            progress.update(1)
