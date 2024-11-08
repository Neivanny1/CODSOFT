# Task 1
<img src='./pics/todoTask.png'>

## Requirements
    Texteditor
    python3 and pip
## Installation
While inside the todo folder run below commands:
1. To create virtual env
```
python3 -m venv venv
```
2. Activate the environment linux systems
```
source venv/bin/activate
```
3. Install dependecies
```
pip install -r requirements.txt
```
4. Run the project:
```
python3 main.py
```
OR
```
uvicorn main:app --reload
```

## PROJECT
<img src='./pics/land.png'>

<img src='./pics/home.png'>
<img src='./pics/home1.png'>

# Running test with pytest
```
pytest --html=report.html
```
Above generates a report of test run and save results in report.html

