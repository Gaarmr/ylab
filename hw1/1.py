import re


p = re.compile(r'(?:https?://)?(?:www\.)?(\w+)')


def domain_name(url):
     if match := p.search(url):
            return match[1]
     return None


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
