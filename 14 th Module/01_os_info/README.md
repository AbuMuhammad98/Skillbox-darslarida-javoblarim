## 1-topshiriq. Tizim haqida axborot
### Nima qilish kerak?
Python operasion tizimi va versiyasi haqida axborot to‘plang. Pastdagi koddan main.pyga nusxa oling va ishga tushiring. Shundy bo‘lganda, agar xatolar yuzaga kelsa, o‘qituvchilar sizga yordam berishi osonroq bo‘ladi.

```python
import platform
import sys

info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(),
    sys.version,
    platform.architecture(),
)
print(info)

with open('os_info.txt', 'w', encoding='utf8') as file:
    file.write(info)
```
### Nima baholanadi?
- Python operasion tizimi va versiyasi haqida axborotga ega «os_info.txt» fayli yaratildi.
