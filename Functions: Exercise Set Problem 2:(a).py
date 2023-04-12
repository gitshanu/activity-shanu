c=input()
def chat(c):
    if len(c)<=200:
        return c
    else:
        b=c[:200]
        return b
print(chat(c))
