'''
作者：雪风
https://www.zhihu.com/question/553621326
链接：https://www.zhihu.com/question/553621326/answer/3263422146
来源：知乎


'''

import requests
import re
import json


class Douyin:

    def __init__(self, rid, stream):
        self.Rid = rid
        self.Stream = stream

    def get_douyin_url(self):
        live_url = f"https://live.douyin.com/{self.Rid}"
        session = requests.Session()

        # Send initial request to obtain __ac_nonce
        headers = {
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "Upgrade-Insecure-Requests": "1",
        }
        oresp = session.get(live_url, headers=headers)
        oresp.close()

        # Extract __ac_nonce from Set-Cookie header
        ac_nonce_match = re.search(r'(?i)__ac_nonce=(.*?);',
                                   oresp.headers.get("Set-Cookie", ""))
        if ac_nonce_match:
            ac_nonce = ac_nonce_match.group(1)
        else:
            return None

        # Set __ac_nonce cookie and send another request
        session.cookies.set("__ac_nonce", ac_nonce)
        resp = session.get(live_url, headers=headers)

        # Extract ttwid from Set-Cookie header
        ttwid_match = re.search(r'(?i)ttwid=.*?;',
                                resp.headers.get("Set-Cookie", ""))
        if ttwid_match:
            ttwid = ttwid_match.group(0)
        else:
            return None

        # Build URL for final request
        url = f"https://live.douyin.com/webcast/room/web/enter/?aid=6383&app_name=douyin_web&live_id=1&device_platform=web&language=zh-CN&enter_from=web_live&cookie_enabled=true&screen_width=1728&screen_height=1117&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=116.0.0.0&web_rid={self.Rid}"
        headers = {
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "Cookie": ttwid,
            "Accept": "*/*",
            "Host": "live.douyin.com",
            "Connection": "keep-alive",
        }

        # Send the final request
        ress = session.get(url, headers=headers)
        ress.close()

        # Parse the JSON response
        data = json.loads(ress.text)
        #print(data)
        status = data.get("data", {}).get("data", [])[0].get("status", 0)

        if status != 2:
            return None

        real_url = ""
        stream_data = data.get("data", {}).get("data", [])[0].get(
            "stream_url", {}).get("live_core_sdk_data",
                                  {}).get("pull_data",
                                          {}).get("stream_data", {})

        value = json.loads(stream_data)
        if self.Stream == "flv":
            real_url = value.get("data", {}).get("origin",
                                                 {}).get("main",
                                                         {}).get("flv", "")
        elif self.Stream == "hls":
            real_url = value.get("data", {}).get("origin",
                                                 {}).get("main",
                                                         {}).get("hls", "")

        return real_url

def generate_txt_file(text):
    with open("douyin_url.txt", "a") as f:
        f.write(f"{text}\n")

def main():
    '''
    输入抖音直播间URL: https://live.douyin.com/10551494183 冬眠眠

    http://pull-hls-f1.douyincdn.com/third/stream-691558388240220843_or4/playlist.m3u8?keeptime=00093a80&wsSecret=4ecc08787053e6c73bd8a4cc85451823&wsTime=663a57c0

    https://live.douyin.com/296953184126 雾
    https://live.douyin.com/996307632607 風
    '''

    #room_url = input("https://live.douyin.com/link: ")
    room_url = "https://live.douyin.com/10551494183"
    quality = "hls"
    # Extract room ID from URL
    match = re.search(r'https://live.douyin.com/(\d+)', room_url)
    if not match:
        return None
    room_id = match.group(1)
    douyin_obj = Douyin(room_id, quality)
    douyin_url = douyin_obj.get_douyin_url()

    if douyin_url:
        print(douyin_url)
        info = room_url + "\n" + douyin_url + "\n"
        #generate_txt_file(info)
    else:
        print("Failed to get URL or URL is empty.")

if __name__ == "__main__":
    main()
