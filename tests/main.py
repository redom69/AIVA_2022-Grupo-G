import unittest
import mymodule
from src.read_video import VideoDetection


class TestMyModule(unittest.TestCase):
    global client_detector
    client_detector = VideoDetection("../dataset/EnterExitCrossingPaths2front.mpg",
                                     "../dataset/results/EnterExitCrossingPaths2front.avi")
    client_detector()

    # Test para comprobar que se haya leido correctamente el video
    def test_read_video(self):
        self.assertTrue(client_detector.videoIsClosed)

    # Test para comprobar si hay posibles clientes en el video
    def test_reconWalker(self):
        self.assertTrue(mymodule.reconWalker(client_detector.bounding_box_test))

    # Test para comprobar cuantos han entrado a la tienda
    def test_enterShopClient(self):
        self.assertEqual(mymodule.enterShop(client_detector), 0)

    # Test para comprobar cuando se han parado en el escaparate
    def test_stopShopClient(self):
        self.assertEqual(mymodule.stopByShop(client_detector), 0)

    # Test para ver cuantos han pasado de largo
    def test_doNotEnterShopClient(self):
        self.assertEqual(mymodule.doNotEnterShop(client_detector), 0)

    #
    # def test_stopByShop3client(self):
    #     self.assertEqual(mymodule.stopByShop(frame), 3)
    #
    # def test_moveByShop3client(self):
    #     self.assertEqual(mymodule.moveByShop(frame), 3)
    #
    # def test_enterExitCrossing(self):
    #     self.assertTrue(mymodule.enterExitCrossing(frame))
    #
    # def test_enterExit(self):
    #     self.assertEqual(mymodule.enterExit(frame), 2)
    #
    # def test_enterStop(self):
    #     clientIn, clientStop = mymodule.enterStop(frame)
    #     self.assertEqual(clientIn, 3)
    #     self.assertEqual(clientStop, 3)
    #
    # def test_moveIn(self):
    #     self.assertTrue(mymodule.moveIn(frame))
    #
    # def test_stopMoveEnter(self):
    #     clientIn, clientStop, clientMove = mymodule.stopMoveEnter(frame)
    #     self.assertTrue(clientIn)
    #     self.assertTrue(clientStop)
    #     self.assertTrue(clientStop)
    #
    # def test_stopMove(self):
    #     clientStop, clientMove = mymodule.stopMove(frame)
    #     self.assertTrue(clientStop)
    #     self.assertTrue(clientStop)


if __name__ == "__main__":
    unittest.main()
