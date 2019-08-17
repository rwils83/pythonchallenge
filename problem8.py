from PIL import Image
import re
import requests
from io import BytesIO
img = Image.open(BytesIO(requests.get("http://www.pythonchallenge.com/pc/def/oxygen.png").content))
row = [img.getpixel((x, img.height /2)) for x in range(img.width)]
row = row[::7]
ords = [r for r, g, b, a in row if r==g==b]
y = re.findall("\d+", "".join(map(chr, ords)))
answer = "".join(map(chr, map(int, y)))
url = f"http://www.pythonchallenge.com/pc/def/{answer}.html"

print(url)