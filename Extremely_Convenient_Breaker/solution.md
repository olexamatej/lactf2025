### Challenge Overview  
We are given a challenge that encrypts a flag and allows us to submit ciphertext for decryption:  

```
nc chall.lac.tf 31180
```

Upon connecting, the server provides an **encrypted flag in hex**, which **changes with each connection**:  

```
Here's the encrypted flag in hex:  
7a7511cdc487192b021eb24c6381d96f85015c96ae9108e2f26512a1244ea10e01bceccc494c95f03d63ac9c486f0d0eb978019c5879603331ce3993daf27bfd
```

It then prompts us:  

```
What ciphertext do you want me to break in an extremely convenient manner? Enter as hex:  
```

However, submitting a short input (e.g., `555555555555`) results in:  

```
Sorry, it's not *that* convenient. Make your ciphertext 64 bytes please.
```


### Understanding the Vulnerability  
1. The encrypted flag changes every time we reconnect.  
2. We cannot directly request the flag to be decrypted.  
3. If we manipulate specific bytes in our ciphertext, the decryption response leaks parts of the flag.  


### Exploiting the System  
To extract the flag, we:  

1. **First, submit a ciphertext with the last 2 bytes changed** and observe the response:  
   ```
   What ciphertext do you want me to break in an extremely convenient manner? Enter as hex:  
   18072398c49beacac3a681414fb3863d77cdacb4d392e5b184c1a5951783c325f613cd19385917ef4c97663b6b0c75f692e8c400ee66f864a6fef7d400d79700  
   ```

   **Response:**  
   ```
   b'lactf{seems_it_was_extremely_convenient_to_get_t\x96\xe75\xc1\xf1\xf0\x16Nt\xfb{\xdb^J\xadU'
   ```

   This gives us most of the flag, except the last part.

2. **Next, change the first 2 bytes to reveal the rest of the flag**:  
   ```
   What ciphertext do you want me to break in an extremely convenient manner? Enter as hex:  
   007bb50c16ba644549401d1b345b9bc60a4730327f4106d8be70471a6a2086bf346344354e685438dcb94e867c0d2dbe7436db6c1a8df554b0eced7a6c4f10eb  
   ```

   **Response:**  
   ```
   b'\xb7\x088a\xecw\x13\xa8\x99\x1d\xd3\x9e\x8b\xbf\xc6vas_extremely_convenient_to_get_the_flag_too_heh}'
   ```

3. **Reconstruct the flag**:  
   ```
   lactf{seems_it_was_extremely_convenient_to_get_the_flag_too_heh}
   ```