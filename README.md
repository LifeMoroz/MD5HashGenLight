# MD5HashGenLight
MD5 Hash Generator

### Installation
Before installation override settings from [config.py](https://github.com/sirseren/MD5HashGenLight/blob/master/config.py) in `local_settings.py`
```
$ python3.6 -mvenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```
### Starting Redis:
```
$ redis-server
```
### Starting the celery worker:
```
$ celery -A tasks worker -l info -P eventlet
```
### Starting the server:
```
$ python3 -m server
```
### Run flake8:
```bash
python3.6 -m flake8 --max-line-length 120 ./
```
### Example:
```
>>>curl -X POST -d "email=user@example.com&url=http://site.com/file.txt" http://localhost:8000/submit
{"id":"0e4fac17-f367-4807-8c28-8a059a2f82ac"}
>>> curl -X GET http://localhost:8000/check?id=000
{"status":"FAILED", "error": "Bad task id"}
>>> curl -X GET http://localhost:8000/check?id=0e4fac17-f367-4807-8c28-8a059a2f82ac
{"status":"STARTED"}
>>> curl -X GET http://localhost:8000/check?id=0e4fac17-f367-4807-8c28-8a059a2f82ac
{"md5":"f4afe93ad799484b1d512cc20e93efd1","status":"SUCCESS","url":"http://site.com/file.txt"}
```
