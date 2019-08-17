# After moving to the next solution I came back and made some changes to this one. The lines that were changed are
# marked. The changes were made to use urllib and re to pull in the text the code would to run against instead of
# having ~1200 lines of random characters
from collections import Counter
import re # this line
import urllib.request as request # this line
my_list = list()
challenge_url = request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode() # this line
x = re.findall("<!--(.*?)-->", challenge_url, re.DOTALL)[-1] # this line
c = dict(Counter(x).most_common()) # this line
for key, value in c.items():
    if 1 == value:
        my_list.append(key)

answer = "".join(my_list)
url = f"http://www.pythonchallenge.com/pc/def/{answer}.html"
print(url)
