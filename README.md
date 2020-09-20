# intel-portfolio-web-page
implementation tasks of Intel 2020 software intern

### run local env

```
python3 -m venv venv
source venv/bin/activate
```

```
pip install -r requirements.txt
```

```
cd portfolio
vi secrets.json
``` 

insert information about database and secret keys, press esc then press ":wq"

```
python manage.py runserver
```

please click "Hello" button on website to check my portfolio


### run test
```
python manage.py test
```


### version control
```sh
python3 ver 3.7.3
django ver 3.1.1
chart.js ver 2.4.0
```