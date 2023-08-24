import re
import time


s = "234aaa23445aaanffomnoffrmno98dfg981110111mno"

ip = re.findall("\d+", s)
# sp = re.findall("\w{2}", s)
# sr = re.findall("(\w)\3*", s)

matcher= re.compile(r'(.)\1*')
sr = [match.group() for match in matcher.finditer(s)]

sd = re.findall("(\d+)\1*", s)

result = re.search(r"([0-9])", s)


mystring_overlap = "abcdeabcdzzzzbcde"
# In case we want to match both abcd and bcde
repeated_ones = set()
pos = 0

start = time.time()

while True:
    match = re.search(r"(.{2,10}).*(\1)+", s[pos:])
    if match:
        print(">>> pos", s[pos:], match.group(1))

        repeated_ones.add(match.group(1))
        pos += match.pos + 1
    else:
        break

end = time.time()

print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")

start = time.time()


# rr = re.findall(r"(\w{2,10}).*(\1)+", s)
nn = re.findall(r"(.{2,10}).*(\1)+", s)

end = time.time()

print("The time of execution of above program is :",
      (end-start) * 10**3, "ms", 10**3, end)


# print(ip)
# print(sp)
# print(sr)
print("sd>>>>>>>", sd)
# print(result.groups())
print("repeated_ones >>>>", repeated_ones)
# print("rr >>>", rr)
print("nn >>>>>", nn)