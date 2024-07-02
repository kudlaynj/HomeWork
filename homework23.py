import re


def all_variants(text):
    text = re.split("", text)
    for i in text:
        print(i)
        if i == "abc":
            yield True


a = all_variants("abc")
for i in a:
    print(i)
print("abc"[0:2])
print("abc"[1:3])
print("abc")
