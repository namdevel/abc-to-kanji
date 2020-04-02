import requests
import re

text_to_convert = 'namdevel'

url = 'https://www.sljfaq.org/cgi/kanjiabc.cgi'
myobj = {'abcin': text_to_convert, 'oneormulti': 0}

x = requests.post(url, data = myobj)
kanji = re.findall(r'<td class="kanji-out">(.*?)</td>', x.text)[0]
print(kanji)