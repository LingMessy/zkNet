import sys
import os
import platform as pf

platform = pf.system().lower()
arch = pf.architecture()[0]
machine = pf.machine()

if platform == 'windows':
    if arch == '64bit' and machine == 'x86_64':
        os.system("pyinstaller -F -w gui.py -n zkNet-oldGui-x64-win.exe")
        os.system("pyinstaller -F -w newGui.py -n zkNet-x64-win.exe")
    elif arch == '32bit' and machine == 'i386':
        os.system("pyinstaller -F -w gui.py -n zkNet-oldGui-x86-win.exe")
        os.system("pyinstaller -F -w newGui.py -n zkNet-x86-win.exe")
    else:
        print("该平台未被支持")

elif platform == 'linux':
    if arch == '64bit' and machine == 'x86_64':
        os.system("pyinstaller -F -w gui.py -n zkNet-oldGui-x64-linux.bin")
        os.system("pyinstaller -F -w newGui.py -n zkNet-x64-linux.bin")
    elif arch == '32bit' and machine == 'i386':
        os.system("pyinstaller -F -w gui.py -n zkNet-oldGui-x86-linux.bin")
        os.system("pyinstaller -F -w newGui.py -n zkNet-x86-linux.bin")
    else:
        print("该平台未被支持")

else:
    print("该平台未被支持")

print("当前平台为：%s-%s-%s" % (platform, arch, machine))
