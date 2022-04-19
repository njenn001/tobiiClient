# Tobii Client 

Stream tobii gaze data to kafka brokers

## Prerequisites

    - python 3.8
    - python3-venv
    - python3-pip 


## Usage

After confirming correct Python installations, os dependent instructions are provided below.

### Windows users

1. Clone the repository 

    ```
    git clone https://github.com/njenn001/tobiiClient.git
    ```

2. First install dependencies and create virtual environment by running setup scripts:

    ```
    python app\app.py -e
    ```

3. Activate the virtual environment before using.

    ```
    .\venv\Scripts\activate     
    .\venv\Scripts\python.exe .\app\app.py -h
    ```

4. The application comes with a strict mode and an interactive gui.

    ```
    .\venv\Scripts\python.exe .\app\app.py -g
    .\venv\Scripts\python.exe .\app\app.py -s
    ```

5. Deactivate the virtual environment as such:

    ```
    deactivate 
    ```

### Linux users

1. Clone the repository 

    ```
    git clone https://github.com/njenn001/tobiiClient.git
    ```

2. First install dependencies and create virtual environment by running setup scripts:

    ```
    python app/app.py -e
    ```

3. Activate the virtual environment before using.

    ```
    source ./venv/bin/activate     
    ./venv/Scripts/python.exe ./app/app.py -h
    ```

4. The application comes with a strict mode and an interactive gui (on applicable machines).

    ```
    ./venv/Scripts/python.exe ./app/app.py -s
    ```

5. Deactivate the virtual environment as such:

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
        
    - Vincent Houston 
        - vincent.e.houston@nasa.gov
## Sources

- https://www.tobiipro.com/
- https://www.tobiipro.com/learn-and-support/learn/
- https://developer.tobiipro.com/python/python-getting-started.html 