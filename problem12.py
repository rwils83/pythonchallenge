from PIL import Image as i

pic = i.open('cave.jpg')
(w, h) = pic.size

even = i.new('RGB', (w // 2, h // 2))
odd = i.new('RGB', (w // 2, h // 2))

for x in range(w):
    for y in range(h):
        p = pic.getpixel((x,y))
        if (x+y)%2 == 1:
            odd.putpixel((x // 2, y // 2), p)
        else:
            even.putpixel((x // 2, y // 2), p)

even.save('even.jpg')
odd.save('odd.jpg')

url = "http://www.pythonchallenge.com/pc/return/evil.html"
even.show()

print(url)