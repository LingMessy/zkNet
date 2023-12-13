import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import ctypes
import platform
from zkNet import zkNet
import tools
from make import version

root = tk.Tk()

if platform.system().lower() == "windows":
    # windows平台根据系统设置进行缩放适应高dpi

    # 调用api设置成由应用程序缩放
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    # 调用api获得当前的缩放因子
    ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
    # 设置缩放因子
    root.tk.call("tk", "scaling", ScaleFactor / 75)

elif platform.system().lower == "linux":
    pass

root.update()

root.geometry("400x300")

root.title("zkNet-v%s" % version)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
# root.rowconfigure(0, weight=1)

ttk.Label(root, text="账号 : ").grid(row=0, column=0)

ttk.Label(root, text="密码 : ").grid(row=1, column=0)

usernameEntry = ttk.Entry(root)

passwdEntry = ttk.Entry(root, show="*")

usernameEntry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W + tk.E, columnspan=2)

passwdEntry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W + tk.E, columnspan=2)

# 分割线
ttk.Separator(root, orient=tk.HORIZONTAL).grid(
    row=3, column=0, sticky=tk.W + tk.E, columnspan=3
)


def msgBox(mtype, title, text):
    if mtype == "info":
        tk.messagebox.showinfo(title, text)
    elif mtype == "warn":
        tk.messagebox.showwarning(title, text)
    elif mtype == "err":
        tk.messagebox.showerror(title, text)
    else:
        tk.messagebox.showerror(title, "无法确定消息类型，软件出现bug，请提issuses反馈")


def authAsPhone():
    net = zkNet(usernameEntry.get(), passwdEntry.get())
    r = net.autoWebAuth("phone")
    msgBox(r[0], r[0], r[1])
    # print("authAsPhone")


def authAsPC():
    net = zkNet(usernameEntry.get(), passwdEntry.get())
    r = net.autoWebAuth("pc")
    msgBox(r[0], r[0], r[1])
    # print("auth as pc")


def authIP():
    net = zkNet(usernameEntry.get(), passwdEntry.get())
    r = net.autoQuickAuthShare(ipEntry.get())
    msgBox(r[0], r[0], r[1])

    # print("auth ip")


def showMore():
    text = "我目前专注于将技术转化为实际收益，若有对计算机领域拥有兴趣与相关技能（如电子、网络、软件等），并且怀揣创新思路的同学，我诚挚地邀请您一同研究交流学习做大做强。如果我的微信号无法联系，请您查阅GitHub发布主页以获取最新信息。任何问题或建议，也都欢迎在GitHub上提出issues，期待与您的交流与合作。"
    github = "Github页面：https://github.com/LingMessy/zkNet"
    msgBox("info", "加入我们", text + "\n" + github)


ttk.Button(root, text="认证本机为手机", width=10, command=authAsPhone).grid(
    row=4, column=0, columnspan=3, sticky=tk.W + tk.E, padx=10, pady=5
)

ttk.Button(root, text="认证本机为电脑", width=10, command=authAsPC).grid(
    row=5, column=0, columnspan=3, sticky=tk.W + tk.E, padx=10, pady=5
)

ttk.Button(root, text="认证以下IP为电脑", width=10, command=authIP).grid(
    row=6, column=0, columnspan=3, sticky=tk.W + tk.E, padx=10, pady=5
)

ttk.Label(root, text="指定 IP : ").grid(row=7, column=0)

ipEntry = ttk.Entry(root)

ipEntry.grid(row=7, column=1, padx=10, pady=5, sticky=tk.W + tk.E, columnspan=2)

ttk.Separator(root, orient=tk.HORIZONTAL).grid(
    row=8, column=0, sticky=tk.W + tk.E, columnspan=3
)

cacheTool = tools.cache()
startupTool = tools.startup4Win()

cacheInfoVar = tk.BooleanVar()
cacheInfoVar.set(cacheTool.checkCache())

startupVar = tk.BooleanVar()
startupVar.set(startupTool.checkStartup())

if cacheInfoVar.get():
    infoDict = cacheTool.readCache()
    if infoDict is not None:
        usernameEntry.delete(0, tk.END)
        passwdEntry.delete(0, tk.END)
        ipEntry.delete(0, tk.END)

        usernameEntry.insert(0, infoDict["username"])
        passwdEntry.insert(0, infoDict["passwd"])
        ipEntry.insert(0, infoDict["ip"])


def cacheInfoClick():
    if cacheInfoVar.get():
        infoDict = {
            "username": usernameEntry.get(),
            "passwd": passwdEntry.get(),
            "ip": ipEntry.get(),
        }

        cacheTool.cacheInfo(infoDict=infoDict)
    else:
        cacheTool.removeCache()


def startupClick():
    msgBox(
        "warn",
        "提示:",
        "为了实现该功能，程序会在启动目录里添加脚本，该操作可能会被杀软误报，导致程序被杀软删除。经测试，如果频繁切换该功能会被自带的defender识别为木马导致程序被删除。",
    )
    startupTool.updateStartup(startupVar.get())


ttk.Checkbutton(root, text="记住信息", variable=cacheInfoVar, command=cacheInfoClick).grid(
    row=9, column=0, columnspan=1, sticky=tk.W + tk.E, padx=10, pady=5
)

ttk.Checkbutton(
    root, text="开机自启(仅限exe)", variable=startupVar, command=startupClick
).grid(row=9, column=1, columnspan=1, sticky=tk.W + tk.E, padx=10, pady=5)

ttk.Button(root, text="加入我们", width=10, command=showMore).grid(
    row=9, column=2, columnspan=1, sticky=tk.E, padx=10, pady=5
)


def closeWindow():
    if cacheInfoVar.get():
        infoDict = {
            "username": usernameEntry.get(),
            "passwd": passwdEntry.get(),
            "ip": ipEntry.get(),
        }

        cacheTool.cacheInfo(infoDict=infoDict)

    startupTool.updateStartup(startupVar.get())

    root.destroy()


root.protocol("WM_DELETE_WINDOW", closeWindow)

tk.mainloop()
