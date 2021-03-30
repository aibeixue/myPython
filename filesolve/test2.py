with open('D:\code\myPython\\aa.txt',) as f:
    text=f.read()
    print(text)
    text2=''.join([s for s in text.splitlines(True) if s.strip()])
    print(text2)
