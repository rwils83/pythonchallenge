from urllib.request import urlopen
import re

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

num = "12345"
#num = str(16044/2)

pattern = re.compile("and the next nothing is (\d+)")

while True:
    content = urlopen(uri % num).read().decode('utf-8')
    # print(content)
    if content != "peak.html": # had to run the program without this to find that I needed peak.html
        match = pattern.search(content)
        if match == None:
            num = str(16044/2)
        else:
            num = match.group(1)
    else:
        print(f"http://www.pythonchallenge.com/pc/def/{content}")
        break
