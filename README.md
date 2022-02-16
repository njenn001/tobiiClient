# Tobii Client 

Stream tobii gaze data to kafak brokers

## System Requiements 
    - python 3.8
    - Tkinter 
    - tobii_research 


## Usage

After confirming correct Python 3.8.2 installation, os dependent instructions are provided below.

### Windows users
First install dependencies and create virtual environment by running setup scripts:

```
python setup.py 
python app\app.py -s 
```

Activate the virtual environment before using. A help script is provided with the application.

```
.\venv\Scripts\activate     
python app\app.py -h
```


Deactivate the virtual environment as such:

```
deactivate 
```

### Linux users
First create virtual environment and install dependencies by running setup scripts:

```
python setup.py 
python app/app.py -s 
```

Activate the virtual environment before using. A help script is provided with the application.

```
source ./venv/bin/activate      
./venv/bin/python app/app.py -h
```


Deactivate the virtual environment as such:

```
deactivate 
```


## Acknowledgments


### Code Contributors

    - Noah Jennings 
        - njenn001@odu.edu

### Authors

    - Noah Jennings
        - njenn001@odu.edu

## Sources

- https://www.tobiipro.com/
- https://www.tobiipro.com/learn-and-support/learn/
- https://developer.tobiipro.com/python/python-getting-started.html 