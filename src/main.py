import read_video

if __name__ == '__main__':
    client_detector = read_video.VideoDetection("../dataset/EnterExitCrossingPaths1front.mpg",
                                                "../dataset/results/EnterExitCrossingPaths1front.avi")
    client_detector()
