import os
import platform as pf

version = "0.9.1"

platform = pf.system().lower()
arch = pf.architecture()[0]
machine = pf.machine()

if __name__ == "__main__":
    if platform == "windows":
        # TODO 有待补充，测试过的平台可以加到这里
        winX64Machine = ["AMD64"]
        winX86Machine = []

        if arch == "64bit" and machine in winX64Machine:
            os.system("pyinstaller -F -w gui.py -n zkNet-v%s-x64-win.exe" % version)

        elif arch == "32bit" and machine in winX86Machine:
            os.system("pyinstaller -F -w gui.py -n zkNet-v%s-x86-win.exe" % version)

        else:
            print("该平台未被支持")

    elif platform == "linux":
        # TODO 有待补充，测试过的平台可以加到这里
        linuxX64Machine = ["x86_64"]
        linuxX86Machine = []
        if arch == "64bit" and machine == "x86_64":
            os.system("pyinstaller -F -w gui.py -n zkNet-v%s-x64-linux.bin" % version)

        elif arch == "32bit" and machine == "i386":
            os.system("pyinstaller -F -w gui.py -n zkNet-v%s-x86-linux.bin" % version)

        else:
            print("该平台未被支持")

    else:
        print("该平台未被支持")

    print("当前平台为：%s-%s-%s" % (platform, arch, machine))
