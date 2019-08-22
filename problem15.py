from PIL import Image
import requests

r = requests.get('http://www.pythonchallenge.com/pc/return/wire.png', auth=("huge", "file"))
print(r)
with open("test.png", "wb") as f:
    f.write(r.content)
im = Image.open('test.png')
delta = [(1,0),(0,1),(-1,0),(0,-1)]
out = Image.new('RGB', [100,100])
x,y,p = -1,0,0
d = 200
while d/2>0:
    for v in delta:
        steps = d // 2
        for s in range(steps):
            x, y = x + v[0], y + v[1]
            out.putpixel((x, y),im.getpixel((p,0)))
            p += 1
        d -= 1
out.save('problem15_result.jpg')
# result is pic of a cat
answer = "cat"
url = f"http://www.pythonchallenge.com/pc/return/{answer}.html"
print(url)
# oops guess we weren't quite done. Maybe his name?
answer = "uzi"
url = f"http://www.pythonchallenge.com/pc/return/{answer}.html"
print(url)