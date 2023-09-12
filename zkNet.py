import requests
import json
import hashlib
# import time


def stringToMd5(v: str, coding='utf-8') -> str:
    md5 = hashlib.md5()
    md5.update(v.encode(coding))
    value = md5.hexdigest()
    return value


class zkNet:

    def __init__(self,
                 userid,
                 passwd,
                 host="1.1.1.1",
                 port='8888',
                 wlanacname="zax_hzstu"):
        self.userid = userid
        self.passwd = passwd
        self.passmd5 = stringToMd5(passwd)
        self.host = host
        self.port = port
        self.url = 'http://' + host + ':' + port

        self.wlanacname = wlanacname

    def getCurDevIp(self) -> str:
        url = 'http://' + self.host
        x = requests
        r = x.get(url, allow_redirects=False)
        rtext = r.text

        start = rtext.find("wlanuserip=") + 11
        end = rtext[start:].find("&")
        ip = rtext[start:start + end]

        return ip

    def webAuth(self, platform: str = 'phone') -> (str, str):
        if platform == 'phone':
            ua = r'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
        # elif platform == 'pc':
        else:
            ua = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'

        headers = {
            'Upgrade-Insecure-Requests': '1',
            'Connection': 'keep-alive',
            # 'Referer': r'http://1.1.1.1:8888/webauth.do?wlanacip=192.16.100.1&wlanacname=zax_hzstu&wlanuserip=10.51.68.157&mac=80:05:88:71:a9:85&vlan=0&url=http://1.1.1.1',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Origin': 'http://1.1.1.1:8888',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept':
            r'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            # 'Host':'1.1.1.1:8888',
            'User-Agent': ua,
        }
        session = requests.session()
        session.headers.update(headers)

        # 认证上网
        postData = r'hostIp=http%3A%2F%2F127.0.0.1%3A8081%2F&loginType=&auth_type=0&isBindMac1=0&pageid=1&templatetype=1&listbindmac=0&recordmac=0&isRemind=0&loginTimes=&groupId=&distoken=&echostr=&url=http%3A%2F%2F1.1.1.1&isautoauth=&notice_pic_float=%2Fportal%2Fuploads%2Fpc%2Fhb_pay%2Fimages%2Frrs_bg.jpg'
        postData += '&userId={}&passwd={}'.format(self.userid, self.passwd)
        try:
            r = session.post(
                self.url +
                r'/webauth.do?wlanacip=192.16.100.1&wlanacname=zax_hzstu&wlanuserip=10.51.68.157&mac=80:05:88:71:a9:85&vlan=0&url=http://1.1.1.1',
                data=postData)
        except requests.exceptions.RequestException as e:
            return ('error', '请求错误，请检查网络状态：' + str(e))

        if '<div class="login_out">' in r.text:
            return ('info', '认证成功')
        else:
            return ('err', '认证可能失败：检查账号密码或手动确认认证状态')

    def quickAuthShare(self, ip: str) -> (str, str):

        session = requests.session()
        # session.headers.update(headers)

        try:
            # 认证上网
            quickAuthShare = session.get(
                self.url + "/quickAuthShare.do?wlanacip=&wlanacname=" +
                self.wlanacname + "&userId=" + self.userid + "&passwd=" +
                self.passwd + "&mac=&wlanuserip=" + ip)

            data = json.loads(quickAuthShare.text)
            loginmsg = data["message"]
        except requests.exceptions.RequestException as e:
            return ('err', '请求错误，请检查网络连接：' + str(e))

        except Exception as e:
            return ('err', 'json 解析错误：' + str(e))

        if loginmsg == "认证成功" or "重复认证" in loginmsg:
            return ('info', '认证成功')
        else:
            # print(loginmsg)
            return ('err', '认证失败，请检查IP地址是否正确')


if __name__ == '__main__':

    net = zkNet('202110000', '666666', wlanacname='zax_hzoffice')

    # 两种认证方式

    # # 认证本机为手机
    r = net.webAuth('phone')
    print(r)
    # # 认证本机为 PC
    # net.webAuth('pc')

    # # 指定 IP 认证为 PC
    # net.quickAuthShare("10.51.70.27")
    # # 本机本机 IP 认证为 PC
    # net.quickAuthShare(net.getCurDevIp())
