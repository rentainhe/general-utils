import re
with open("a.md","r",encoding="utf8") as f:
    s = f.read()
t = re.sub(r"\!\[(.*)\]\(.*?\)\1",r"$\1$",s)

with open("b.md","w") as f:
    f.write(t)