cipher = "wklv phvvdjh lv qrw wrr kdug wr euhdn"
plain = ""
for c in cipher:
    if c == ' ':
        plain += c
    else:
        plain += chr(ord(c) - 3)
print (plain)
