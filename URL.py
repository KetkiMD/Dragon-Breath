from urllib.request import urlopen

page = urlopen("https://monkeytype.com/")
print(page.headers)

