import requests
import json

print('http://www.pythonchallenge.com/pc/return/evil2.jpg')
print('http://www.pythonchallenge.com/pc/return/evil3.jpg')
print('http://www.pythonchallenge.com/pc/return/evil4.jpg')

r = requests.get('http://www.pythonchallenge.com/pc/return/evil4.jpg', auth=('huge', 'file')).text
print(r)

data = open("evil2.gfx", "rb").read()

for each in range(5):
     open('%d.jpg' % each, 'wb').write(data[each::5])

answer = "http://www.pythonchallenge.com/pc/return/disproportional.html"
print(answer)

