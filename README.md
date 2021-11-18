# Auto Registration for UW
Python script to automatically register for class using SLN codes and Selenium automation.
## Set Up 
### .env
Create a .env file with your UW NET ID Username and Password
```
USERNAME=YOUR_USER_NAME
PASSWORD=YOUR_PASSWORD
```
### Change Classes
Replace slns with slns of classes that you want to register for
```python
slns = ["17168", "17169"]
```
### Install Requirements
```
pip install requirements.txt
```
## Install Chrome Driver
### Mac
```
brew install --cask chromedriver
```
### Windows
download the latest [chromedriver.exe](https://sites.google.com/chromium.org/driver/downloads?authuser=0)
### Replace the following lines
```python
browser = webdriver.Chrome()
```
with
```python
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(executable_path="path/to/chromedriver.exe", chrome_options=options)
```

# Usage
```  
python main.py
```

