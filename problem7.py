import zipfile, re

f = zipfile.ZipFile("channel.zip")
num = '90052'
comments = []

while True:
    content = f.read(num + ".txt").decode("utf-8")
    print(content)
    comments.append(f.getinfo(num + ".txt").comment.decode("utf-8"))
    match = re.search("Next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)
print("".join(comments))

url = "http://www.pythonchallenge.com/pc/def/hockey.html"
print(url)
# look at the letters that make the ascii art : they are : O makes h, x makes o, g makes k, e makes e, n makes y

print("http://www.pythonchallenge.com/pc/def/oxygen.html")