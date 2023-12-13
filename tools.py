import os
import sys

# print(filePath)
# d = {'username': '123131231', 'passwd': '1233333', 'ip': '120.1.1.1'}


class cache:
    homePath = os.path.expanduser("~")
    cachePath = os.path.join(homePath, ".cache", "zkNet")
    filePath = os.path.join(cachePath, "zkNet.cache")

    def checkCache(self) -> bool:
        if os.path.exists(self.filePath):
            return True
        else:
            return False

    def cacheInfo(self, infoDict: dict[str, str]):
        dictStr = ""
        for k, v in infoDict.items():
            dictStr += "%s = %s\n" % (k, v)

        if not os.path.exists(self.cachePath):
            os.makedirs(self.cachePath)

        with open(self.filePath, "w", encoding="utf-8") as f:
            f.write(dictStr)

    def readCache(self) -> dict[str, str] | None:
        if not os.path.exists(self.filePath):
            return None

        with open(self.filePath, "r", encoding="utf-8") as f:
            dictStr = f.read()

        rDict = {}
        for line in dictStr.strip().splitlines():
            k, v = tuple(i.strip() for i in line.split("="))
            rDict[k] = v

        return rDict

    def removeCache(self):
        if os.path.exists(self.filePath):
            os.remove(self.filePath)
            if os.listdir(self.cachePath) == []:
                os.rmdir(self.cachePath)


# 可能被杀软误杀
class startup4Win:
    homePath = os.path.expanduser("~")
    zkNetPath = os.path.realpath(sys.argv[0])
    batPath = r"AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    batPath = os.path.join(homePath, batPath, "zkNet.bat")
    batContent = r'start "" "%s"' % zkNetPath

    def updateStartup(self, startup: bool):
        if not startup:
            self.delStartup()
            return

        if not self.checkStartup():
            self.addStartup()

    def checkStartup(self) -> bool:
        if not os.path.exists(self.batPath):
            return False

        with open(self.batPath, "r") as f:
            content = f.read()

        if content != self.batContent:
            return False

        return True

    def addStartup(self):
        with open(self.batPath, "w") as f:
            f.write(self.batContent)

    def delStartup(self):
        if os.path.exists(self.batPath):
            os.remove(self.batPath)


# addToStartup4Win()
