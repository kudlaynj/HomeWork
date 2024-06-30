import re


def all_variants(text):
    text = re.split("", text)
    for i in text:
        print(i)
        if i == "abcdefghij":
            yield True


a = all_variants("abc")
for i in a:
    print(i)
