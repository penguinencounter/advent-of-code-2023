import re

translate = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
su = 0
with open("1.in") as f:
    b = f.read()
    b = re.sub(
        r"^.*?(one|two|three|four|five|six|seven|eight|nine|\d)", r"\1 ", b, flags=re.M
    )
    b = re.sub(
        r" .*(one|two|three|four|five|six|seven|eight|nine|\d).*?$",
        r"\1",
        b,
        flags=re.M,
    )
    # handle duplicates
    b = re.sub(r"^(.*) .*$", r"\1\1", b, flags=re.M)
    for k, v in translate.items():
        b = b.replace(k, str(v))
    print(sum(map(int, b.splitlines())))
