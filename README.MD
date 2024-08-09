# Instagram Avto Followers

Bu Python skripti avtomatik ravishda [SMMPanel](https://smmpanel.com) saytida akkaut yaratadi va nakrutka xizmatga buyurtma beradi. Skript Selenium kutubxonasidan foydalanadi va CAPTCHAni chetlab o'tish va avtomatlashtirish uchun "Buster" extension dan foydalanadi.


Chrome orqali ishga tushirish uchun sistemangizga mos drayverni yuklab oling.

## Instagram akkauntni kiritish

`main.py` faylidan 162 qatordan instagram foydalanuvchi nomingizni kiritishni unutmang:

```python
# Masalan: cristiano
link_input.send_keys('https://instagram.com/cristiano/')
```

## O'rnatish

   ```bash
   git clone https://github.com/s4evers/Instagram-Auto-Followers.git
   cd Instagram-Auto-Followers
   pip install -r requirements.txt
```
## Ishga tushirish

  ```bash
python3 main.py
