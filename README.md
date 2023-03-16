# Monitoring youtube channels

Creates index.html (and sites.new) files listing the videos that have changed since the last time the parseyt.py script was run.
There is no need to sign in to your account.

![](screenshot.png)

### Installation

```
./install
```

  * If necessary, downloads and installs google chrome, selenium, chromedriver
  * Only installer supports x64 debian based systems, but python script - any linux

### Tuning

Correct the parsedb.py file for your set of monitoring channels.

```python
urls={ \
    "https://www.youtube.com/channel/UC9MK8SybZcrHR3CUV4NMy2g/videos":("",""),
    "https://www.youtube.com/c/VertDiderScience/videos":("",""),
    "https://www.youtube.com/c/vdud/videos":("",""),
    "https://www.youtube.com/user/fulllux/videos":("",""),
    "https://www.youtube.com/c/foo52ru/videos":("",""),
}
```
### How to use

```
python3 ./parsedb.py
```

The script updates parsedb.py every time it is run. When restarted, only new videos puts into index.html and sites.new.

```
/usr/bin/google-chrome-stable ./index.html
```
or
```
./sites.new
```

# Монитороинг youtube каналов

Создает index.html (и sites.new) файлы со списком изменившихся видео с момента последнего запуска скрипта parseyt.py.
Нет необходимости входить в свой аккаунт.

![](screenshot.png)

### Установка

```
./install
```
 * При необходимости скачивает и устанавливает google chrome, selenium, chromedriver
 * Установщик поддерживает только debian based x64 системы, а питоновский скрипт - любые

### Настройка

Измените parsedb.py в соотвествии с необходимым набором каналов для мониторинга.

```python
urls={ \
    "https://www.youtube.com/channel/UC9MK8SybZcrHR3CUV4NMy2g/videos":("",""),
    "https://www.youtube.com/c/VertDiderScience/videos":("",""),
    "https://www.youtube.com/c/vdud/videos":("",""),
    "https://www.youtube.com/user/fulllux/videos":("",""),
    "https://www.youtube.com/c/foo52ru/videos":("",""),
}
```
### Использование

```
python3 ./parsedb.py
```

Скрипт обновляет parsedb.py, при каждом запуске. При повторных запусках, в index.html и в sites.new попадают только новые видео.

```
/usr/bin/google-chrome-stable ./index.html
```
or
```
./sites.new
```
