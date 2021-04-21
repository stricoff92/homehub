
# Smart Mirror

### 3rd Party Data
The smart mirror uses data from several free APIs, some of which require registration.
Register for API keys for the following services:
 - [openweathermaps](https://home.openweathermap.org/users/sign_up)
 - [wordnik](https://developer.wordnik.com/)
 - [calendarific](https://calendarific.com/signup)

### Part List
1. Raspberry Pi 3 or better
2.  ~21" 1920x1080 Monitor in Portrait Mode & HDMI cable
3. 18"x24" 2 way mirror
4. (Optional) Frame for mirror, hardware to attach frame and mount to wall


### Raspberry Pi Setup
1. Boot up the pi and connect it to wifi & enable SSH server
2. Update Software
```bash
$ sudo apt update
$ sudo apt full-upgrade
```
3. Add the below options to `/boot/config.txt`
```bash
# Force display into portrait mode
display_rotate=3
gpu_mem=128
```
4. Uncomment `disable_overscan=1` in `/boot/config.txt` if the display has a black border
5. Install xscreensaver `sudo apt-get install xscreensaver` and disable screen sleep
6. Install unclutter `sudo apt-get install unclutter` and add the below option to `/etc/xdg/lxsession/LXDE-pi/autostart`
```bash
@unclutter -idle 0
```
7. Build current stable version of SQLITE3 from source [downloads](https://www.sqlite.org/download.html). The version included on the Pi is likely incompatable with Django.
8. Build Python3.6.X or better from source [downloads](https://www.python.org/downloads/)
```bash
# when building python ensure the correct version of SQLITE is avaiable
$ sudo LD_RUN_PATH=/usr/local/lib ./configure --enable-optimizations
$ sudo LD_RUN_PATH=/usr/local/lib make altinstall
```
9. Install pip and virtualenv
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ sudo python3.6 get-pip.py
$ pip3.6 install virtualenv
```
10. Install Nodejs and NPM
```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo bash -
$ sudo apt install nodejs
```

### Setup Code
1. Clone the repo
```bash
$ cd ~
$ git pull https://github.com/stricoff92/homehub.git
$ cd homehub
```
2. Install Python dependancies
```bash
$ virtuelenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```
3. Install Node dependancies, build the angular app
```
$ cd homehub/website/appclient
$ npm install
$ npm run-script buildprod
$ cd ..; cd ..
$ ./manage.py collectstatic
```
4. Create `applocals.py` file in `homehub/homehub/homehub/`
```python
# Example applocals.py
# DO NOT COMMIT THIS FILE

SECRET_KEY = 'SECRET KEY GOES HERE'
ENV = "PROD"
DEBUG = False
ALLOWED_HOSTS = ["*"]

APP_PORT = "8000"

CHROME_DRIVER_PATH = ""
WEATHER_API_KEY = "SECRET KEY GOES HERE"
WORDNIK_API_KEY = "SECRET KEY GOES HERE"
CALENDARIFIC_API_KEY = "SECRET KEY GOES HERE"

PUSHOVER_APP_TOKEN = "SECRET KEY GOES HERE"
PUSHOVER_USER_TOKEN = "SECRET KEY GOES HERE"

```
5. Migrate the database
```
$ ./manage.py migrate
```
6. Create a super user
```
$ ./manage.py createsuperuser
```
7. Populate 3rd party data
```bash
$ ./manage.py set_hubstate_isactive_to_true
$ ./manage.py update_bike_cache
$ ./manage.py update_holiday_cache
$ ./manage.py update_vulnerabilities_records
$ ./manage.py update_weather_cache
$ ./manage.py update_wotd_cache
```

### Schedule Tasks
```
# root's crontab

# Restart the Pi every morning
0 7 * * * /sbin/shutdown -r +1
```

```
# Pi's crontab

# Restart the Webapplication and start polling for 3rd party data
@reboot /home/pi/homehub/homehub/boot_homehub_rpi >> /home/pi/bootlog.log

# Put monitor to sleep and stop polling for 3rd party data
59 23 * * * /home/pi/homehub/homehub/boot_off_homehub_rpi >> /home/pi/bootlog.log

# WEATHER
*/2 * * * * /home/pi/homehub/env/bin/python /home/pi/homehub/homehub/manage.py update_weather_cache

# BIKES
*/5 * * * * /home/pi/homehub/env/bin/python /home/pi/homehub/homehub/manage.py update_bike_cache

# WOTD 02:10 daily
10 2 * * * /home/pi/homehub/env/bin/python /home/pi/homehub/homehub/manage.py update_wotd_cache

# vulnerabilities 02:20 daily
20 2 * * * /home/pi/homehub/env/bin/python /home/pi/homehub/homehub/manage.py update_vulnerabilities_records

# holidays on January 1, at 06:30
30 6 1 1 * /home/pi/homehub/env/bin/python /home/pi/homehub/homehub/manage.py update_holiday_cache
```

