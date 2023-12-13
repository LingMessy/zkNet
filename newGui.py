import customtkinter as ctk
from zkNet import zkNet
import tkinter as tk

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = ctk.CTk()

root.geometry("300x300")

root.title("zkNet")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

ctk.CTkLabel(root, text="账号 : ").grid(row=0, column=0)

ctk.CTkLabel(root, text="密码 : ").grid(row=1, column=0)

e1 = ctk.CTkEntry(root)

e2 = ctk.CTkEntry(root, show="*")

e1.grid(row=0, column=1, padx=10, pady=5, sticky=ctk.W + ctk.E)

e2.grid(row=1, column=1, padx=10, pady=5, sticky=ctk.W + ctk.E)

# 分割线
# ctk.Separator(root, orient=tk.HORIZONTAL).grid(row=3,
#                                                column=0,
#                                                sticky=tk.W + tk.E,
#                                                columnspan=2)


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
    net = zkNet(e1.get(), e2.get())
    r = net.autoWebAuth("phone")
    msgBox(r[0], r[0], r[1])
    # print("authAsPhone")


def authAsPC():
    net = zkNet(e1.get(), e2.get())
    r = net.autoWebAuth("pc")
    msgBox(r[0], r[0], r[1])
    # print("auth as pc")


def authIP():
    net = zkNet(e1.get(), e2.get())
    r = net.autoQuickAuthShare(e3.get())
    msgBox(r[0], r[0], r[1])

    # print("auth ip")


def showMore():
    text = "我目前专注于将技术转化为实际收益，若有对计算机领域拥有兴趣与相关技能（如电子、网络、软件等），并且怀揣创新思路的同学，我诚挚地邀请您一同研究交流学习做大做强。如果我的微信号无法联系，请您查阅GitHub发布主页以获取最新信息。任何问题或建议，也都欢迎在GitHub上提出issues，期待与您的交流与合作。"
    github = "Github页面：https://github.com/LingMessy/zkNet"
    msgBox("info", "加入我们", text + "\n" + github)


ctk.CTkButton(root, text="认证本机为手机", width=10, command=authAsPhone).grid(
    row=4, column=0, columnspan=2, sticky=ctk.W + ctk.E, padx=10, pady=5
)

ctk.CTkButton(root, text="认证本机为电脑", width=10, command=authAsPC).grid(
    row=5, column=0, columnspan=2, sticky=ctk.W + ctk.E, padx=10, pady=5
)

ctk.CTkButton(root, text="认证以下IP为电脑", width=10, command=authIP).grid(
    row=6, column=0, columnspan=2, sticky=ctk.W + ctk.E, padx=10, pady=5
)

ctk.CTkLabel(root, text="指定 IP : ").grid(row=7, column=0)

e3 = ctk.CTkEntry(root)

e3.grid(row=7, column=1, padx=10, pady=5, sticky=ctk.W + ctk.E)

# ctk.Separator(root, orient=tk.HORIZONTAL).grid(row=8,
#                                                column=0,
#                                                sticky=tk.W + tk.E,
#                                                columnspan=2)

ctk.CTkButton(root, text="加入我们", width=10, command=showMore).grid(
    row=9, column=1, columnspan=1, sticky=ctk.E, padx=10, pady=5
)

root.mainloop()
