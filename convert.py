import requests
import re
import sys

text_to_convert = sys.argv[1]

url = 'https://www.sljfaq.org/cgi/kanjiabc.cgi'
myobj = {'abcin': text_to_convert, 'oneormulti': 0}

x = requests.post(url, data = myobj)
kanji = re.findall(r'<td class="kanji-out">(.*?)</td>', x.text)[0]
print(kanji)