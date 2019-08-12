import requests

answer = "map".translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"))

url = f"http://www.pythonchallenge.com/pc/def/{answer}.html"
print(url)