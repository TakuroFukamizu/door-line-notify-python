# door-line-notify-python


## setup

### middleware

```
$ sudo apt-get install python-rpi.gpio
```

### auto run

open `/etc/rc.local` file and insert a follow line at before of `exit 0`

```text:/etc/rc.local
python /home/pi/src/door-line-notify-python/main.py &

```


## execute

```
$ sudo python main.py
```