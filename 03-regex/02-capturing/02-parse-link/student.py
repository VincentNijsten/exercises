import re


def parse_link(string):
    match = re.fullmatch(r'<a href="(.*)">(.*)</a>', string)
    if match:
        caption, url = match.groups()
        return (caption, url)
    else:
        return None

print(parse_link('<a href="title">url.be</a>'))