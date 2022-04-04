import read_video

if __name__ == '__main__':
    client_detector = read_video.VideoDetection("../dataset/OneLeaveShopReenter1front.mpg",
                                                "../dataset/results/OneLeaveShopReenter1front.avi")
    client_detector()

    print("Entran ", client_detector.entran, " clientes")
    print("Pasan de largo ", client_detector.no_pasan, " clientes")
    print("Esperan ", client_detector.esperan, " clientes")
