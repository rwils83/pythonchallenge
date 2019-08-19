import itertools
x = "1"
for n in range(30):
    x = "".join([str(len(list(j))) + i for i,j in itertools.groupby(x)])
answer = len(x)

url = f"http://www.pythonchallenge.com/pc/return/{answer}.html"

print(url)