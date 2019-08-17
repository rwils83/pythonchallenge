import pickle
import urllib.request as request

x = pickle.load(request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
for line in x:
    print("".join([k*v for k, v in line]))
url = "http://www.pythonchallenge.com/pc/def/channel.html"
print(url)
