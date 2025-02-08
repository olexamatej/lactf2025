
### **Challenge Overview**  
The challenge presents a website with **two eyes** that guide us to different places where tokens are hidden. Our goal is to **find all tokens** by searching various locations in a web application.  

![eyes](imgs/image.png)  

---
### **Finding the Tokens**  


#### **Token in HTML Source Code**  
By viewing the **page source** (`Ctrl + U` in a browser), we find a token hidden in the raw HTML.  

---

#### **Token in JavaScript Code**  
Inspecting the **JavaScript files** loaded by the page, we find another token. This can be done using browser dev tools (`F12 → Sources` or `Ctrl + Shift + I`).  

---

#### **Token in the Console**  
By opening the **JavaScript console** (`F12 → Console`), another token is revealed. Sometimes, developers leave debug messages that expose secrets.  

---

#### **Token in Cookies**  
Checking the **browser cookies** (`F12 → Application → Storage → Cookies`), we find another token stored in the cookies.  

---

#### ** Token in Stylesheets**  
Inspecting the **CSS files** (`F12 → Sources`), we find a token embedded in a stylesheet.  
![CSS Token](imgs/image-1.png)  

---

#### **Token in Headers**  
By inspecting the **HTTP response headers**, another token is revealed. This can be done using:  
- Browser Dev Tools (`F12 → Network → Select a request → Headers`)  
- `curl` or `wget`:  
  ```bash
  curl -I https://i-spy.chall.lac.tf/
  ```
  ![Header Token](imgs/image-3.png)  

---

#### **Token in `robots.txt`**  

![Robots Token](imgs/image-4.png)  


The website's `robots.txt` file contains a **hidden file path**.  

Visiting `https://i-spy.chall.lac.tf/robots.txt`:  
```
User-agent: *
Disallow: /a-magical-token.txt
```
Fetching `https://i-spy.chall.lac.tf/a-magical-token.txt` reveals:  
```
3FB4C9545A6189DE5DE446D60F82B3AF
```  


---

#### **Token in `sitemap.xml`**  
A `sitemap.xml` file tells search engines which pages to index.  
Visiting `https://i-spy.chall.lac.tf/sitemap.xml`:  
![Sitemap Token](imgs/image-5.png)  

---

#### **Token from a DELETE Request**  
By sending a **DELETE request** to the website, we get another token:  
```bash
curl -X DELETE https://i-spy.chall.lac.tf/
```
Response:  
```
You DELETED MY WEBSITE!!!!! HOW DARE YOU????? 32BFBAEB91EFF980842D9FA19477A42E
```

---

#### **Token in a TXT DNS Record**  
Some tokens can be hidden in **DNS TXT records**. We can check them using `nslookup`:  
```bash
nslookup -type=TXT i-spy.chall.lac.tf
```
Response:  
```
i-spy.chall.lac.tf text = "Token: 7227E8A26FC305B891065FE0A1D4B7D4"
```
