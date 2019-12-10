__author__ = 'qi.zhang01'
import logging, os, time
import shutil
class Getlog():

    def __init__(self, name, lever="1"):
        self.logger = logging.getLogger(name)
        if lever == "1":
            self.logger.setLevel(logging.INFO)
        else:
            self.logger.setLevel(logging.ERROR)
        timestr = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        self.filePath = os.path.join("..\log", name+timestr)
        print(self.filePath)
        with open(self.filePath, "w"):
            pass

    def fileHand(self, filePath):
        self.hander = logging.FileHandler(filePath)
        self.hander.setFormatter(logging.Formatter("%(asctime)s--%(levelname)s--%(message)s", "%Y/%m/%d %H:%M:%S"))
        return self.hander

    def startLog(self):
        self.logger.addHandler(self.fileHand(self.filePath))
        return self.logger

    def stopLog(self):
        pass

    @classmethod
    def delLog(cls, path="..\log"):
        for i in os.listdir(path):
            os.remove(os.path.join(path, i))
        return "OJBK"

if __name__ == "__main__":

    Getlog.delLog()
