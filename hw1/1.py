# import re


# p = re.compile(r'(?:https?://)?(?:\w+\.)?(\w+)(?:\.\w+)+')


# def domain_name(url):
#      if match := p.search(url):
#             return match[1]
#      return None

def domain_name(url: str):
    if url[:4] == 'http':
        res = url.split('/')[2]
        if res[:3] == 'www':
            res = res.split('.')[1]
        else:
            res = res.split('.')[0]
    else:
        res = url.split('.')[1]
    return res

assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
assert domain_name("aboba.youtube.com") == "youtube"
