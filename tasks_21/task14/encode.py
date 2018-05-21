def encode(str):
    global codes
    op = ""
    for ch in str:
        op +=codes[ch]
    return op
a="sandeep"
print encode(a)
