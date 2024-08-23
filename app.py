from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello")
def hello2():
    return "This is a test"

@app.route('/m')
def static_html():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>Page Title</title>
    </head>
    <body>
    
    <h1>This is a Heading</h1>
    <p>This is a paragraph.</p>
    
    </body>
    </html>
    """
    return html_content

@app.route('/dy1')
def static_html1():
    html_content1 = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=0.5, maximum-scale=1.0, user-scalable=0" />
    <meta charset="utf-8">
    <meta name="referrer" content="no-referrer">
    <link rel="icon" href="https://cdn.glitch.global/8ec61d84-f524-405b-85fd-2f601dbe9197/706835E4-7F99-4179-BF0A-2BF98E00A9C5.png?v=1654703270026" type="image/x-icon" />
    <!-- Modified 6/1/2024-->
    <title>分享视频/分享視頻</title>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/lozad/dist/lozad.min.js"></script>
    <script>
    document.addEventListener('DOMContentLoaded', function() {
    const observer = lozad(); // lazy loads elements with default selector as '.lozad'
    observer.observe();
    });
    </script>

    <style>
    h1,
    h2 {
    text-align: center;
    color: white;
    text-shadow: 2px 2px #0000ff
    }

    body {
    background-image: url('https://images.ctfassets.net/cnu0m8re1exe/6rkPDdVnHFMDz29XtjWXuY/fc31afa24685cb2babdb2a32dc2bfa7d/shutterstock_169805951.jpg');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center top;
    /* Position the image at the top center */
    /*background-size: 100% 3000px;*/
    /* width 100% and height 500px */

    }

    #playlist-container {
    display: flex;
    justify-content: space-between;
    width: 800px;
    height: 600px;
    margin: 0 auto;
    }

    #videoPlayer {
    height: 600px;
    width: auto;
    }

    iframe {
    margin-left: 10px;
    display: none;
    /* Hide the iframe initially */
    height: 630px;
    width: 350px;
    border: solid 1px gray;
    }

    #playlist {
    border: solid 2px orange;
    width: 100%;
    /* Set width to 100% to fill the container */
    background-color: #f2f2f2;
    padding: 10px;
    height: 600px;
    /* Set a fixed height */
    overflow-y: auto;
    /* Enable vertical scrolling */

    /* Scrollbar styling */
    scrollbar-width: thin;
    /* For Firefox */
    scrollbar-color: gray;
    /* For Firefox */

    }

    #playlist::-webkit-scrollbar {
    width: 7px;
    height: 3px;
    }

    #playlist::-webkit-scrollbar-track {
    height: 5px !important;
    }

    #playlist::-webkit-scrollbar-thumb {
    border-radius: 4px !important;
    height: 3px;
    background: #41617D !important;
    box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.5) !important;
    }

    #playlist div {
    margin: 10px;
    cursor: pointer;
    padding: 5px;
    padding-top: 6.9px;
    border: solid 1px gray;

    }

    #playlist div:hover {
    background-color: #ddd;
    border: solid 1px black;
    }

    #reverseButton {
    height: 100px;
    padding: 0px 20px;
    border-radius: 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
    font-size: 16px;
    border: solid 2px white;
    }

    #reverseButton:hover {
    background-color: #45a049;
    border: solid 2px blue;
    color: blue;
    }

    ul {
    text-decoration-style: none;
    }

    li::marker {
    color: white;
    }

    a {
    color: #00aaff;
    text-shadow: 0.5px 1px white;
    }

    #playing-text {
    color: white;
    text-align: center;
    margin-top: 30px;
    }

    span1 {
    color: white;
    }

    pre {
    margin: 10px;
    cursor: pointer;
    padding: 5px;
    padding-top: 6.9px;
    border: solid 1px gray;

    }

    .switch {
    font-size: 10px;
    border-radius: 20px;

    }

    #loopDiv{
    padding:0px 10px 10px 20vw;
    background-color:rgba(242, 247, 242,0.5);
    width:100%;
    }

    .switchLoop {
    position: relative;
    display: inline-block;
    width: 60px;
    height: 34px;
    }

    .switchLoop input { 
    opacity: 0;
    width: 0;
    height: 0;
    }

    .slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    -webkit-transition: .4s;
    transition: .4s;
    }

    .slider:before {
    position: absolute;
    content: "";
    height: 26px;
    width: 26px;
    left: 4px;
    bottom: 4px;
    background-color: white;
    -webkit-transition: .4s;
    transition: .4s;
    }

    input:checked + .slider {
    background-color: #2196F3;
    }

    input:focus + .slider {
    box-shadow: 0 0 1px #2196F3;
    }

    input:checked + .slider:before {
    -webkit-transform: translateX(26px);
    -ms-transform: translateX(26px);
    transform: translateX(26px);
    }

    /* Rounded sliders */
    .slider.round {
    border-radius: 34px;
    }

    .slider.round:before {
    border-radius: 50%;
    }

    footer {
    text-align: center;
    padding: 100px;
    justify-content: center;
    align-items: center;
    display: flex;
    }

    footer a {
    padding: 0 10px;
    margin-left: 25px;
    margin-right: 25px;
    }

    footer a:first-child {
    margin-left: 0;
    /* No margin on the left for the first link */
    }

    footer a:last-child {
    margin-right: 0;
    /* No margin on the right for the last link */
    }
    </style>
    </head>

    <body>

    <h1>欢迎来到新网站：链接库</h1>
    <h2>歡迎來到新網站：連結庫</h2>



    <div style="display:flex; align-items:center;justify-content: center;">

    <button id="reverseButton">
    点击即可反转播放列表
    <br />
    Click to Reverse Playlist
    <br />
    點擊即可反轉播放列表
    </button>
    <p style="background-color:white;margin-left: 10px;padding:10px;">Hi!!! Click video name on right to play<br /> 您好 点击右侧视频名击即播放</p>
    </div>

    <script>
    document.addEventListener("DOMContentLoaded", function() {
    // Disable zooming on double click for the reverseButton
    var reverseButton = document.getElementById("reverseButton");
    reverseButton.addEventListener("dblclick", function(event) {
    event.preventDefault();
    });
    });
    </script>
    <center>

    <button id="switchType1" style="" class="switch">
    点击即可切换到音乐视频
    <br />
    Click for Music Video Playlist
    <br />
    點擊即可切換到音樂視頻
    </button>

    <button id="switchType2" style="" class="switch">
    点击即可切换到娱乐视频
    <br />
    Click for Entertainment Video Playlist
    <br />
    點擊即可切換到娛樂視頻
    </button>

    <div id="playing-text" style="margin-top: 30px;color:white;"> <!--Added video name-->
    Currently playing video name goes here
    </div>

    </center>

    <div id="playlist-container">
    <div id="videoPlayerContainer"> <!-- Added container for video and iframe -->
    <video class="lozad" id="videoPlayer" controls playsinline>
    <source src="" type="video/mp4">
    </video>
    <iframe class="lozad" allowfullscreen oncontextmenu="return false;" sandbox="allow-top-navigation allow-same-origin allow-forms allow-scripts"></iframe>
    </div>
    <div id="playlist">
    </div>
    </div>
    <div id="loopDiv">
    <span>music video loop</span><br/>
    <label class="switchLoop">
    <input type="checkbox" id="loopSwitch">
    <span class="slider round" onclick="toggleLoop()"></span>
    </label></div>



    <script>
    let playlist1 = [{
    name: "冬眠眠replay1.mp4",
    src: "https://player.odycdn.com/api/v3/streams/free/冬眠眠replay1/ae696bfe6f975ab2d1af310a15d2bf03d622c950/5da3e5.mp4",
    type: "music"
    },
    {
    name: "冬眠眠replay2.mp4",
    src: "https://player.odycdn.com/api/v3/streams/free/冬眠眠replay2/67d369435655bb387b8dbf15c3e35971a12f913b/fc6815.mp4",
    type: "music"
    },
    {
    name: "冬眠眠replay3.mp4",
    src: "https://player.odycdn.com/api/v3/streams/free/冬眠眠replay3/13de4aa43e95ac5f19ebb2e3034696dcc1ac5dae/455724.mp4",
    type: "music"
    },
    {
    name: "合唱.mp4",
    src: "https://player.odycdn.com/api/v3/streams/free/合唱/9dd7cb2e80b9d529a0685eb99ea3c91aa3506f2d/c12e02.mp4",
    type: "music"
    },
    {
    name: "杭州接档上班.mp4",
    src: "https://player.odycdn.com/api/v3/streams/free/杭州接档上班/0f290bd2970d75a5bc7d1dbda51a5557e74ddbcd/11f0e3.mp4",
    type: "music"
    },
    {
    name: "陈replay1.mp4 图片+mp3",
    src: "https://player.odycdn.com/api/v3/streams/free/陈replay1/0eb0325b62422439b55c029d8f49dbf2a7876553/1095d4.mp4",
    type: "music"
    },
    {
    name: "风老师replay1.mp4 图片+mp3",
    src: "https://player.odycdn.com/api/v3/streams/free/风老师replay1/7df654cbfebb04719a080016b2fdde449d8fa41d/88d687.mp4",
    type: "music"
    },
    {
    name: "风老师replay2.mp4",
    src: "https://player.odycdn.com/api/v3/streams/free/风老师replay2/6a626d3cc15e65065d04e0f78c6291e0469fb15b/2b962f.mp4",
    type: "music"
    },
    {
    name: "风老师replay3.mp4",
    src: "https://player.odycdn.com/api/v3/streams/free/风老师replay3/35b3d9892aed90b3350a492c6fee99dda4622a3e/14da13.mp4",
    type: "music"
    },
    {
    name: "冬眠眠二创节目（上）抖音播放器",
    src: "https://open.douyin.com/player/video?vid=7357025582187629861",
    type: "fun"
    },
    {
    name: "冬眠眠二创节目（中 1）抖音播放器",
    src: "https://open.douyin.com/player/video?vid=7357385769469611301",
    type: "fun"
    },
    {
    name: "冬眠眠二创节目（中 2）抖音播放器",
    src: "https://open.douyin.com/player/video?vid=7357392215934569766",
    type: "fun"
    },
    {
    name: "冬眠眠二创节目（中 3）抖音播放器",
    src: "https://open.douyin.com/player/video?vid=7357407735455010057",
    type: "fun"
    },
    {
    name: "冬眠眠二创节目 (早恋被六哥发现) 抖音播放器",
    src: "https://open.douyin.com/player/video?vid=7357422301639445797",
    type: "fun"
    },
    {
    name: "冬眠眠replay4.mp4",
    src: "https://player.odycdn.com/api/v3/streams/free/冬眠眠replay4/83c48786d505911ba427b854872a9b2e36879c54/e23985.mp4",
    type: "music"
    },
    {
    name: "冬眠眠接档1.mp4",
    src: "https://player.odycdn.com/api/v3/streams/free/冬眠眠接档1/546b34f384b3a387eaf0271dd072146807db74e6/b309e0.mp4",
    type: "music"
    },
    {
    name: "W老师Short1",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download.mp4",
    type: "music"
    },
    {
    name: "W老师Short2",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(1).mp4",
    type: "music"
    },
    {
    name: "W老师Short3",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(2).mp4",
    type: "music"
    },
    {
    name: "W老师Short4",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(3).mp4",
    type: "music"
    },
    {
    name: "W老师Short5",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(4).mp4",
    type: "music"
    },
    {
    name: "W老师Short6",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(5).mp4",
    type: "music"
    },
    {
    name: "W老师Short7",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(6).mp4",
    type: "music"
    },
    {
    name: "W老师Short8",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(7).mp4",
    type: "music"
    },
    {
    name: "W老师Short9",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(8).mp4",
    type: "music"
    },
    {
    name: "W老师Short10",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(9).mp4",
    type: "music"
    },
    {
    name: "W老师Short11",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(10).mp4",
    type: "music"
    },
    {
    name: "W老师Short12",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(11).mp4",
    type: "music"
    },
    {
    name: "W老师Short13",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(12).mp4",
    type: "music"
    },
    {
    name: "W老师Short14",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(13).mp4",
    type: "music"
    },
    {
    name: "W老师Short15",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(14).mp4",
    type: "music"
    },
    {
    name: "W老师Short16",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(15).mp4",
    type: "music"
    },
    {
    name: "W老师Short17",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(16).mp4",
    type: "music"
    },
    {
    name: "W老师Short18",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(17).mp4",
    type: "music"
    },
    {
    name: "W老师Short19",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(18).mp4",
    type: "music"
    },
    {
    name: "W老师Short20",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(19).mp4",
    type: "music"
    },
    {
    name: "W老师Short21",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(20).mp4",
    type: "music"
    },
    {
    name: "W老师Short22",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(21).mp4",
    type: "music"
    },
    {
    name: "W老师Short23",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(22).mp4",
    type: "music"
    },
    {
    name: "W老师Short24",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(23).mp4",
    type: "music"
    },
    {
    name: "W老师Short25",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(24).mp4",
    type: "music"
    },
    {
    name: "W老师Short26",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(25).mp4",
    type: "music"
    },
    {
    name: "W老师Short27",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(26).mp4",
    type: "music"
    },
    {
    name: "W老师Short28",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(27).mp4",
    type: "music"
    },
    {
    name: "W老师Short29",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(28).mp4",
    type: "music"
    },
    {
    name: "W老师Short30",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(29).mp4",
    type: "music"
    },
    {
    name: "W老师Short31",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(30).mp4",
    type: "music"
    },
    {
    name: "W老师Short32",
    src: "https://s3.us-east-2.amazonaws.com/www.jjbird.personal.com/download+(31).mp4",
    type: "music"
    },
    {
    name: "W老师Short33",
    src: "//www.douyin.com/aweme/v1/play/?video_id=v0d00fg10000cpfeicfog65jtu6vjg1g",
    type: "music"

    },
    {
    name: "冬眠眠replay5",
    src: "https://player.odycdn.com/api/v3/streams/free/vcompress_94/c51fb7d4060873cadff1565c2983677263a52b6c/12b149.mp4",
    type: "music"
    },
    {
    name: `冬眠2024.05.27个播
    22:18-01:27录屏
    BiliBili抖音播放器`,
    src: "https://player.bilibili.com/player.html?bvid=BV1Ex4y1p7Mp&autoplay=0&high_quality=1&autoplay=0",
    type: "fun"
    },
    {
    name: `冬眠2024.05.30个播
    21:06-00:00录屏1
    BiliBili抖音播放器`,
    src: "https://player.bilibili.com/player.html?bvid=BV15T421q7Ak&autoplay=0&high_quality=1&autoplay=0",
    type: "fun"
    },
    {
    name: `冬眠2024.05.30个播
    21:06-00:00录屏2
    BiliBili抖音播放器`,
    src: "https://player.bilibili.com/player.html?bvid=BV1ZM4m167BA&autoplay=0&high_quality=1&autoplay=0",
    type: "fun"
    },
    {
    name: `冬眠2024.05.31个播
    21:53-23:31录屏
    BiliBili抖音播放器`,
    src: "https://player.bilibili.com/player.html?bvid=BV1rs421M7Pp&autoplay=0&high_quality=1&autoplay=0",
    type: "fun"
    }
    /*
    { name: "Video 45", src: "", type: "music" },
    { name: "Video 46", src: "", type: "music" },
    { name: "Video 47", src: "", type: "music" },
    { name: "Video 48", src: "", type: "music" },
    { name: "Video 49", src: "", type: "music" }，
    { name: "Video 50", src: "", type: "music" }
    { name: "Video 51", src: "", type: "music" },
    { name: "Video 52", src: "", type: "music" },
    { name: "Video 53", src: "", type: "music" },

    */

    /* 冬眠眠二创节目（上） 7357019897307696393*/
    ];

    //playlist.reverse(); // Optionally reverse the playlist

    window.addEventListener("DOMContentLoaded", () => {
    let playlist = playlist1;

    let switchType1Button = document.getElementById("switchType1");
    let switchType2Button = document.getElementById("switchType2");


    let videoPlayer = document.getElementById("videoPlayer");
    let playlistContainer = document.getElementById("playlist");
    let reverseButton = document.getElementById("reverseButton");
    let playingText = document.getElementById("playing-text"); // Reference to the center div
    let currentVideoIndex = 0;
    let currentVideoName = playlist[currentVideoIndex].name; // Get the name of the current video

    function playNextVideo() {
    // Function to play the next video in the playlist
    currentVideoIndex = (currentVideoIndex + 1) % playlist.length;
    currentVideoName = playlist[currentVideoIndex].name;
    playingText.textContent = currentVideoName; // Update the center div with the current video name
    if (playlist[currentVideoIndex].src.includes("bilibili")) {
    document.querySelector("iframe").style.width = "550px";
    } else {
    document.querySelector("iframe").style.width = "350px";
    }
    if (playlist[currentVideoIndex].src.includes("douyin.com") || playlist[currentVideoIndex].src.includes("bilibili")) {
    // If the next video is a Douyin URL, show it in an iframe
    document.getElementById("videoPlayer").style.display = "none";
    document.querySelector("iframe").style.display = "block";
    document.querySelector("iframe").src = playlist[currentVideoIndex].src;
    } else {
    // Otherwise, play it in the video player
    document.getElementById("videoPlayer").style.display = "block";
    document.querySelector("iframe").style.display = "none";
    videoPlayer.src = playlist[currentVideoIndex].src;
    videoPlayer.load();
    videoPlayer.play();
    }
    }

    videoPlayer.addEventListener("ended", playNextVideo); // Event listener for video end

    // Check if the default URL is a Douyin URL
    if (playlist[0].src.includes("bilibili")) {
    document.querySelector("iframe").style.width = "550px";
    } else {
    document.querySelector("iframe").style.width = "350px";
    }
    if (playlist[0].src.includes("douyin.com") || playlist[0].src.includes("bilibili")) {
    document.getElementById("videoPlayer").style.display = "none";
    document.querySelector("iframe").style.display = "block";
    document.querySelector("iframe").src = playlist[0].src;
    } else {
    document.querySelector("iframe").style.display = "none";
    document.getElementById("videoPlayer").style.display = "block";
    videoPlayer.src = playlist[0].src;
    videoPlayer.load();
    // videoPlayer.play(); // Optionally play the first video automatically
    }
    currentVideoName = playlist[currentVideoIndex].name;
    playingText.textContent = currentVideoName; // Update the center div with the current video name

    function renderPlaylist() {
    // Function to render the playlist items dynamically
    playlistContainer.innerHTML = ""; // Clear previous playlist items
    //document.querySelector("ul").innerHTML = ""; // Clear previous list items
    document.getElementById("ul1").innerHTML = "";

    playlist.forEach((video, index) => {
    // Loop through the playlist array
    let divItem = document.createElement("div");
    let playlistItem = divItem.appendChild(document.createElement("pre"));
    playlistItem.style.overflow = "hidden";
    playlistItem.textContent = video.name;
    playlistItem.addEventListener("click", () => {

    // Event listener for clicking on a playlist item
    if (video.src.includes("bilibili")) {
    document.querySelector("iframe").style.width = "550px";
    } else {
    document.querySelector("iframe").style.width = "350px";
    }
    if (video.src.includes("douyin.com") || video.src.includes("bilibili")) {
    // If clicked item is a Douyin URL, show it in an iframe
    videoPlayer.pause();
    document.getElementById("videoPlayer").style.display = "none";
    document.querySelector("iframe").style.display = "block";
    document.querySelector("iframe").src = video.src;
    // Pause the iframe audio
    document.querySelector("iframe").contentWindow.postMessage('{"event":"command","func":"pauseVideo","args":""}', '*');
    } else {
    // Otherwise, play it in the video player
    document.getElementById("videoPlayer").style.display = "block";
    document.querySelector("iframe").style.display = "none";
    document.querySelector("iframe").src = "https://jjbird1.glitch.me";
    videoPlayer.src = "";
    videoPlayer.src = video.src;
    videoPlayer.load();
    videoPlayer.play();
    }
    currentVideoIndex = index;
    currentVideoName = playlist[currentVideoIndex].name;
    playingText.textContent = currentVideoName; // Update the center div with the current video name

    });

    playlistContainer.appendChild(playlistItem); // Append playlist item to container

    // Dynamically add list items with URLs from the playlist array
    /*
    let listItem = document.createElement("li");
    let link = document.createElement("a");
    link.href = video.src;
    link.textContent = video.name;
    link.target = "_blank";
    listItem.appendChild(link);
    document.getElementById("ul1").appendChild(listItem);
    */
    });
    }

    renderPlaylist(); // Render the playlist items initially

    reverseButton.addEventListener("click", () => {
    // Event listener for reversing the playlist
    playlist.reverse(); // Reverse the playlist array
    renderPlaylist(); // Render the reversed playlist

    // Check if the default URL is a Douyin URL after reversing
    if (playlist[0].src.includes("bilibili")) {
    document.querySelector("iframe").style.width = "550px";
    } else {
    document.querySelector("iframe").style.width = "350px";
    }
    if (playlist[0].src.includes("douyin.com") || playlist[0].src.includes("bilibili")) {
    document.getElementById("videoPlayer").style.display = "none";
    document.querySelector("iframe").style.display = "block";
    document.querySelector("iframe").src = playlist[0].src;
    } else {
    document.querySelector("iframe").style.display = "none";
    document.getElementById("videoPlayer").style.display = "block";
    videoPlayer.src = playlist[0].src;
    videoPlayer.load();
    }
    currentVideoName = playlist[currentVideoIndex].name;
    playingText.textContent = currentVideoName; // Update the center div with the current video name
    });

    switchType1Button.addEventListener("click", function() {
    switchType1Button.style.display = "none"; // Hide switchType1Button
    switchType2Button.style.display = "inline-block"; // Show switchType2Button

    // Filter the playlist to show only music videos
    let musicPlaylist = playlist1.filter(video => video.type === "music");
    playlist = musicPlaylist;
    renderPlaylist();
    });

    switchType2Button.addEventListener("click", function() {
    switchType1Button.style.display = "inline-block"; // Show switchType1Button
    switchType2Button.style.display = "none"; // Hide switchType2Button

    // Filter the playlist to show only entertainment videos
    let funPlaylist = playlist1.filter(video => video.type === "fun");
    playlist = funPlaylist;
    renderPlaylist();
    });
    var checkbox = document.getElementById('loopSwitch'); 
    checkbox.checked = false;
    console.log("first",checkbox.checked);

    });
    function toggleLoop() {
    var checkbox = document.getElementById('loopSwitch'); 
    var video = document.getElementById('videoPlayer');
    console.log(checkbox.checked)
    video.loop = !checkbox.checked;
    var status = video.loop ? 'enabled' : 'disabled';
    console.log("loop: ", status);

    }

    </script>


    <div style="padding:0px 0px 30px 0px;">

    </div>

    <div>
    <a>Sources/来源/來源: </a>
    <ul>
    <li>
    <a>Screen recordings/录屏</a>
    </li>

    <li>
    <a href="https://www.iesdouyin.com/share/user/MS4wLjABAAAAysBiGQixREPwlw2s_ZlP9qwvpz6VJgI-PjfeUIZD1rZ8NPKsqZI6l7XuL-INBQX7" target="_blank">𝑇.冬眠¹²²¹</a>
    <span1>抖音号：Dongm1221</span1>
    </li>

    <li>
    <a href="https://www.iesdouyin.com/share/user/MS4wLjABAAAA002m0PmxPg3vMI7aJxmnEzyE4BlM-2KHhaSzw0uYkgguQfjVmhgo-uP1c8i61c0y" target="_blank">☀️永顷~¹²²¹</a>
    <span1>抖音号：YXYYQ0514</span1>
    </li>

    <li>
    <a href="https://www.iesdouyin.com/share/user/MS4wLjABAAAAZD6P-sArTs8tHnDV4OxiwqqxcGGeLvpsnp2vOWx-yA4" target="_blank">网友w. (W老师)</a>
    <span1>抖音号：wait_u.ww</span1>
    </li>

    <li>
    <a href="https://www.iesdouyin.com/share/user/MS4wLjABAAAAE4OL9MY22vtu9H6lF6XlS4OYRYBZAzAHmyCgavJSlvE" target="_blank">风声声🎸 (风老师)</a>
    <span1>抖音号：FS961006</span1>
    </li>

    <li>
    <a href="https://www.iesdouyin.com/share/user/MS4wLjABAAAAJxRsOyyQhFiOWcNWdeoD_5NawUuBIE46Zet4GVTdULI" target="_blank">小玫瑰🥀</a>
    <span1>抖音号：73699154222</span1>
    </li>
    <li>
    <a href="https://space.bilibili.com/1271861688" target="_blank">冬眠の录屏</a>
    <span1>B站号：1271861688</span1>
    </li>
    </ul>
    </div>

    <ul id="ul1">
    <!-- The list items will be dynamically generated here -->
    </ul>

    <div style="padding:0px 0px 100px 0px;">

    </div>
    <!--

    <script>
    if (window.location.protocol !== 'https:') {
    var currentUrl = window.location.href;
    var secureUrl = currentUrl.replace(/^http:/, 'https:');
    window.location.replace(secureUrl);
    }
    </script>

    4/13/2024 in process of getting a ssl certificate; 90day certificate
    update:5/30/2024 update new expiration: 8/28/2024
    update:8/18/2024 update new expiration: 11/16/2024
    updated:8/23/2024 to render
    -->
    <footer>

    <a href="hls.html" target="_self">(Mp4,Hls,Flv)Video player</a>
    <a href="checker.html" target="_self">Checker.html</a>

    </footer>
    </body>

    </html>
    """
    return html_content2

if __name__ == '__main__':
    app.run(debug=True)
