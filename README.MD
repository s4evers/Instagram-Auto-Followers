# Instagram Avto Followers

Bu Python skripti avtomatik ravishda [SMMPanel](https://smmpanel.com) saytida akkaut yaratadi va nakrutka xizmatga buyurtma beradi. Skript Selenium kutubxonasidan foydalanadi va CAPTCHAni chetlab o'tish va avtomatlashtirish uchun "Buster" extension dan foydalanadi.


Chrome orqali ishga tushirish uchun sistemangizga mos drayverni yuklab oling.

## Важно обратить внимание

В коде, расположенном в файле `main.py` на строке 162, происходит ввод ссылки в поле:

```python
# main.py, строка 162
link_input.send_keys('https://instagram.com/cs.mer6/')

## O'rnatish

   ```bash
   git clone https://github.com/s4evers/Instagram-Auto-Followers.git
   cd Instagram-Auto-Followers
   pip install -r requirements.txt
```
## Ishga tushirish

  ```bash
python3 main.py
