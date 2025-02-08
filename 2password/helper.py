
leaked_bytes = [
'0x75687b667463616c',
'0x66635f327265746e',
'0x7d38367a783063',]

flag = "".join([bytes.fromhex(h[2:]).decode()[::-1] for h in leaked_bytes])

print(flag)