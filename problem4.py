import re
import urllib.request as request

challenge_url = request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
x = re.findall("<!--(.*?)-->", challenge_url, re.DOTALL)[-1]

answer = "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", x))
url = f"http://www.pythonchallenge.com/pc/def/{answer}.php" # after going to .html, the answer redirected to .php
print(url)
