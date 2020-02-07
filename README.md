# python-crash-course

<p>Includes Chapters for Python Crash Course session. </p>


## What will you learn:

<ul>
   <li>Python Essentials</li>
   <li>Creating Server</li>
   <li>Writing REST API</li>
   <li>Writing Python Scripts</li>
</ul>


## Prerequisites:

#### 1. Install Python:
```
$ brew install python3
```
- More details:
- https://docs.python-guide.org/starting/install3/osx/


#### 2. Install PyCharm
https://www.jetbrains.com/pycharm/download/#section=mac


## Post clone

###### Create virtual environment
```
$ python3 -m venv venv
```

###### Install dependencies
```
$ pip3 install -r requirements.txt
```


###### Run Uvicorn Server
```
$ uvicorn expense:app --host 0.0.0.0 --port 8000
```
