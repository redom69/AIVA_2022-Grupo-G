import read_video
import numpy as np
from time import time

if __name__ == '__main__':
    start_time = time()

    client_detector = read_video.VideoDetection("../dataset/OneShopOneWait2front.mpg",
                                                "../dataset/results/OneShopOneWait2front.avi")
    client_detector()
    end_time = time()
    fps = np.round(end_time - start_time, 3)
    print(f"Tiempo de ejecucion del video : {fps}")
