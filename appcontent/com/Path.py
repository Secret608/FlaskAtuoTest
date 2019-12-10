__author__ = 'qi.zhang01'

import sys


class GetPath():

    def __init__(self):
        self.path = self.getGlobalPath('Flask_test')

    def getGlobalPath(self, dirName):
        """
        :get global path
        """
        globalPath = sys.path[0]
        for item in sys.path:
            if item.endswith(dirName):
                globalPath = item
                return globalPath

    def getCurrentPath(self):
        return self.path


if __name__ == '__main__':
    print(GetPath.__module__)