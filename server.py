from flask import Flask, render_template, jsonify
import requests
import json
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/hello")
def hello2():
    return "This is a test"


class Douyin:
    def __init__(self, rid, stream):
        self.Rid = rid
        self.Stream = stream

    def get_douyin_url(self):
        live_url = f"https://live.douyin.com/{self.Rid}"
        session = requests.Session()

        # Send initial request to obtain __ac_nonce
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "Upgrade-Insecure-Requests": "1",
        }
        oresp = session.get(live_url, headers=headers)
        oresp.close()
'''
        # Extract __ac_nonce from Set-Cookie header
        ac_nonce_match = re.search(
            r"(?i)__ac_nonce=(.*?);", oresp.headers.get("Set-Cookie", "")
        )
        if ac_nonce_match:
            ac_nonce = ac_nonce_match.group(1)
        else:
            return None
'''
        # Alternative using string functions
        cookie_header = oresp.headers.get("Set-Cookie", "")
        start_index = cookie_header.find("__ac_nonce=")
        if start_index != -1:
            end_index = cookie_header.find(";", start_index)
            ac_nonce = cookie_header[start_index + len("__ac_nonce=") : end_index]
            ac_nonce_match = ac_nonce  # This is equivalent to re.match object in the original code
        else:
            ac_nonce_match = None
        # Set __ac_nonce cookie and send another request
        session.cookies.set("__ac_nonce", ac_nonce)
        resp = session.get(live_url, headers=headers)
'''
        # Extract ttwid from Set-Cookie header
        ttwid_match = re.search(r"(?i)ttwid=.*?;", resp.headers.get("Set-Cookie", ""))
        if ttwid_match:
            ttwid = ttwid_match.group(0)
        else:
            return None
'''
        cookie_header = resp.headers.get("Set-Cookie", "")
        start_index = cookie_header.find("ttwid=")
        if start_index != -1:
            end_index = cookie_header.find(";", start_index)
            ttwid = cookie_header[start_index + len("ttwid=") : end_index]
        else:
            return None

        # Build URL for final request
        url = f"https://live.douyin.com/webcast/room/web/enter/?aid=6383&app_name=douyin_web&live_id=1&device_platform=web&language=zh-CN&enter_from=web_live&cookie_enabled=true&screen_width=1728&screen_height=1117&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=116.0.0.0&web_rid={self.Rid}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
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
        
        if data is None:
            return "NoneAvailable"
        
        #status = data.get("data", {}).get("data", [])[0].get("status", 0)
        nested_data = data.get("data", {}).get("data", [])
        if nested_data:
            status = nested_data[0].get("status", 0)
            if status is None:
                return "NoneAvailable"


            if status != 2:
                return "NoneAvailable"

            real_url = ""
            stream_data = (
                data.get("data", {})
                .get("data", [])[0]
                .get("stream_url", {})
                .get("live_core_sdk_data", {})
                .get("pull_data", {})
                .get("stream_data", {})
            )

            value = json.loads(stream_data)


            if self.Stream == "flv":
                real_url = (
                    value.get("data", {}).get("origin", {}).get("main", {}).get("flv", "")
                )
            elif self.Stream == "hls":
                real_url = (
                    value.get("data", {}).get("origin", {}).get("main", {}).get("hls", "")
                )

            return real_url
            
        else:        
            return "NoneAvailable"

       


@app.route("/dy")
def dy():
    """
    输入抖音直播间URL: https://live.douyin.com/10551494183 冬眠眠

    http://pull-hls-f1.douyincdn.com/third/stream-691558388240220843_or4/playlist.m3u8?keeptime=00093a80&wsSecret=4ecc08787053e6c73bd8a4cc85451823&wsTime=663a57c0

    https://live.douyin.com/296953184126 雾
    https://live.douyin.com/996307632607 風
    """

    # room_url = input("https://live.douyin.com/link: ")
    room_url = ["https://live.douyin.com/10551494183"
      ,"https://live.douyin.com/157798460679"
      ,"https://live.douyin.com/717116949591"
      ,"https://live.douyin.com/568345900946"
      ,"https://live.douyin.com/296953184126"
      ,"https://live.douyin.com/996307632607"
      ,"https://live.douyin.com/706382469811"
      ,"https://live.douyin.com/865316633666" 
      ,"https://live.douyin.com/912218533434"
      ,"https://live.douyin.com/269057911447"
      ,"https://live.douyin.com/753041292895"
      ,"https://live.douyin.com/415775074508"
      ,"https://live.douyin.com/375700772866"
      ,"https://live.douyin.com/289351680100"
      ,"https://live.douyin.com/404145744276"
      ,"https://live.douyin.com/439377080585"
      ,"https://live.douyin.com/144046351727"
      ,"https://live.douyin.com/182429874062"

    ]
    name = ["冬眠眠" #10
            , "Chua瞬" #15
            , "抓马" #71
            , "南笙" #56
            , "雾" #29
            , "風" #99
            , "陈小沈" #70
            , "hot club" #86
            , "TCG" #91
            , "radio" #26
            , "佑曦" #75
            , "甜崽⁷" #41
            , "弟弟" #37
            , "夏屿" #28
            , "南北" #40
            , "key" #43
            , "n" #14
            , "不知" #18
           ]
    quality = "hls"
    dy_urls = []

    for x in range(len(name)):
'''
        # Extract room ID from URL
        match = re.search(r"https://live.douyin.com/(\d+)", room_url[x])
        if not match:
            return None
        room_id = match.group(1)
'''
        
        url = room_url[x]
        if url.startswith("https://live.douyin.com/"):
            room_id_start = len("https://live.douyin.com/")
            room_id_end = url.find("/", room_id_start)
            if room_id_end != -1:
                room_id = url[room_id_start:room_id_end]
            else:
                room_id = url[room_id_start:]
        else:
            return None
        douyin_obj = Douyin(room_id, quality)
        douyin_url = douyin_obj.get_douyin_url()
        if douyin_url and douyin_url[0]=="h":
            douyin_url = "https://" + douyin_url[len("http://") :]
            dy_urls.append(douyin_url)
        elif douyin_url is None:
            dy_urls.append('name[x]') 
        else:
            dy_urls.append('name[x]')

    #return {'dy_urls': dy_urls}
    return render_template("s2.html", name=name, urls=dy_urls)

  

if __name__ == "__main__":
    # app.run()
    app.run(host="127.0.0.1", port=5000,debug=True)
