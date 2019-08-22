import xmlrpc.client
conn = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(conn.system.listMethods())

print(conn.system.methodHelp("phone"))

print(conn.system.methodSignature("phone"))

print(conn.phone("Bert"))

answer = conn.phone("Bert").split("-")[1].lower()

url = f'http://www.pythonchallenge.com/pc/return/{answer}.html'
print(url)