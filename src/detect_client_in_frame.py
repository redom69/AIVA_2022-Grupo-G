import cv2
import pandas


class FrameDetection:
    """
    Class implements Yolo5 model to make inferences on a video using OpenCV.
    """

    def __init__(self, frame):
        """
        Initializes the class with the video frame.
        :param frame: Frame detected by the video.
        """
        self.frame = frame
        self.bounding_box = []

    @staticmethod
    def score_frame(frame, model, confiance, max):
        """
        Takes a single frame as input, and scores the frame using yolo5 model.
        :param model: model transfer from yolov5s
        :param frame: input frame in numpy/list/tuple format.
        :return: Labels and Coordinates of objects detected by model in the frame.
        """
        frame = [frame]
        results = model(frame)
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        if len(results.pandas().xyxy[0]) > 0:
            if len(confiance) > 0:
                del confiance[0]
            confiance.append(results.pandas().xyxy[0]['confidence'])
            c = sum(results.pandas().xyxy[0]['confidence']) / len(results.pandas().xyxy[0]['confidence'])
            if c > max:
                return labels, cord, c

        return labels, cord, max

    def plot_boxes(self, results, frame):
        """
        Takes a frame and its results as input, and plots the bounding boxes and label on to the frame.
        :param results: contains labels and coordinates predicted by model on the given frame.
        :param frame: Frame which has been scored.
        :return: Frame with bounding boxes and labels ploted on it, list of x and list of y coordinates.
        """
        bounding_box = []
        self.bounding_box = []
        labels, cord,_ = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        lista_y2 = []
        lista_x2 = []
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.2:
                x1, y1, x2, y2 = int(row[0] * x_shape), int(row[1] * y_shape), int(row[2] * x_shape), int(
                    row[3] * y_shape)
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                self.bounding_box.append([x1, x1, x2, y2])
                lista_y2.append(y2)
                lista_x2.append(x2)
                bounding_box.append([x1, x1, x2, y2])
        return frame, lista_y2, lista_x2, bounding_box

    @staticmethod
    def entran(lista_y2, lista_y2_ant):
        """
        Count the number of people going into the shop.
        :param lista_y2: contains y coordinates of lower right corner from the bounding box (current frame)
        :param lista_y2_ant: contains y coordinates of lower right corner from the bounding box (previous frame)
        :return: number of people going into the shop in a frame
        """
        cont_ent = 0
        for elem in lista_y2:
            if (elem == 140) and (141 in lista_y2_ant):
                cont_ent += 1

        return cont_ent

    @staticmethod
    def pasan(lista_x2):
        """
        Count the number of people walking past the shop window.
        :param lista_x2: contains x coordinates of lower right corner from the bounding box (current frame)
        :return: number of people going through line 1 (c1) and line 2 (c2) in a frame
        """
        c1 = 0
        c2 = 0
        for elem in lista_x2:
            if 99 <= elem <= 101:
                c1 += 1
            elif 324 <= elem <= 326:
                c2 += 1

        return c1, c2

    @staticmethod
    def se_paran(pos_x, anteriores, posicion):
        """
        Count the number of people stopping in front of the shop window. :param pos_x: contains x coordinates of
        lower right corner from the bounding box (current frame) :param anteriores: a list of lists of x coordinates
        of lower right corner from the bounding box (previous 10 frames) :param posicion: x coordinate of lower right
        corner from the bounding box if counter is increased :return: number of people stopping in a frame
        """
        cont_par = 0
        cont = 0
        for x in pos_x:
            if (x != posicion) and (60 < x < 210):
                for lista in list(anteriores):
                    if x in lista:
                        cont += 1
                if cont == 10:
                    cont_par += 1
                    posicion = x

        return cont_par, posicion
