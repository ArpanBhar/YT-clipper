import os
from datetime import datetime
def rs(n):
    n = str(n).split(":")
    t = datetime.strptime(":".join(n),"%M:%S") if len(n) == 2 else datetime.strptime(":".join(n),"%H:%M:%S")
    t2 = datetime.strptime("00:30","%M:%S")
    diff = str(t-t2).split(":")
    try:
        if int(diff[0]) == 0:
            del diff[0]
        diff = ":".join(diff)
        global passed
        passed = True
    except:
        diff = "00:00"
        passed = False
    return diff
link = input("Enter the video link: ")
timestamp = input("Enter the starting time: ")
seek = input("Enter the time to seek: ")
x = os.popen(f"yt-dlp --youtube-skip-dash-manifest -g {link}").read()
x,y = x.split()
cmd = "-ss 30" if rs(timestamp) != "00:00" or (rs(timestamp) == "00:00" and passed == True) else ""
os.system(f"ffmpeg -ss {rs(timestamp)} -i \"{x}\" -ss {rs(timestamp)} -i \"{y}\" -map 0:v -map 1:a {cmd} -t {seek} -c:v libx264 -c:a aac output.mp4")