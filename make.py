#!/usr/bin/env python3

import os
import platform as pf
import sys

version = "0.9.1"

PYTHON = "python"
REQU = " ".join(("requests", "pyinstaller"))

platform = (pf.system().lower(), pf.architecture()[0], pf.machine())


def buildWin64():
    os.system(
        "call wvenv/Scripts/activate.bat && pyinstaller -F -w gui.py -n zkNet-v%s-x64-win.exe"
        % version
    )


def buildWin32():
    os.system(
        "call wvenv/Scripts/activate.bat && pyinstaller -F -w gui.py -n zkNet-v%s-x86-win.exe"
        % version
    )


def buildLinux64():
    os.system(
        "source venv/bin/activate && pyinstaller -F -w gui.py -n zkNet-v%s-x64-linux.bin"
        % version
    )


def buildLinux32():
    os.system(
        "source venv/bin/activate && pyinstaller -F -w gui.py -n zkNet-v%s-x86-linux.bin"
        % version
    )


def runWin():
    os.system("call wvenv/Scripts/activate.bat && python gui.py")


def runLinux():
    os.system("source venv/bin/activate && python gui.py")


def venvWin():
    os.system(
        f"{PYTHON} -m venv wvenv && call wvenv/Scripts/activate.bat && pip install {REQU}"
    )


def venvLinux():
    os.system(
        f"{PYTHON} -m venv venv && source venv/bin/activate && pip install {REQU}"
    )


def cleanWin():
    os.system("rmdir /s /Q build dist __pycache__ venv wvenv & del /Q *.spec")


def cleanLinux():
    os.system("rm -rf build dist *.spec __pycache__ venv wvenv")


# TODO 有待补充，测试过的平台可以加到这里
supportPlatformTable = [
    # system    arch    machine     build    run    venv        clean
    ("windows", "64bit", "AMD64", buildWin64, runWin, venvWin, cleanWin),
    ("linux", "64bit", "x86_64", buildLinux64, runLinux, venvLinux, cleanLinux),
]


def build():
    for i in supportPlatformTable:
        if i[:3] == platform:
            i[3]()
            print("当前平台为：%s-%s-%s" % platform)
            return
    print("当前平台为：%s-%s-%s" % platform)
    print("该平台未被支持")


argvTable = [("build", 3), ("run", 4), ("venv", 5), ("clean", 6)]

if __name__ == "__main__":
    funcIdx = None

    if len(sys.argv) != 2:
        print("useage: python make.py <option>")
        sys.exit(0)

    for arg, fIdx in argvTable:
        if sys.argv[1] == arg:
            funcIdx = fIdx
            break

    if funcIdx is None:
        print("option not support")
        sys.exit(0)

    platformIdx = None
    for i, v in enumerate(supportPlatformTable):
        if v[:3] == platform:
            platformIdx = i
            break

    if platformIdx is None:
        print("platform not support")
        print("该平台未被支持")
        sys.exit(0)

    supportPlatformTable[platformIdx][funcIdx]()

    print("当前平台为：%s-%s-%s" % platform)
