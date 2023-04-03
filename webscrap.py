# I used this code to web scrap some informations on internal system
# The login page asks for username, password+OTP and captcha
# I did not implement automatic captcha solving yet and used a input popup to get OTP, because it comes from a mobile app
# I have changed some information, due to security reasons
# I also changed function names and other references to English - hope to not have broken anything
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import tkinter as tk # used for gui dialog boxes
from tkinter import simpledialog
import os # used to save directly to .txt - not used, after changing to create datagram and .xlsx
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog - PATH
file_path = simpledialog.askstring(title="Output dir",
                                  prompt="Enter complete windows path:") # It will be used to save file

username = 'username'
password = 'password'
url = 'URL_TO_ACCESS_SYSTEM'

# Firefox config
option = Options()
option.add_argument('-headless')
#driver = webdriver.Firefox(options=option)
browser = webdriver.Firefox()

# Function that I used first to sabe to a .txt file
# I used a comma as a separator between itens and a "-" to separate values
#def save_status(status_req,wo,status_wo,tas,support_group):
#    os.chdir(file_path)
#    f = open('status_REQs.txt', "a")
#    status_message = req+"-"+status_req+"-"+wo+"-"+status_wo+"-"+tas+"-"+support_group+"," # these values come from several itens scrapped from the system
#    f.write(status_message)
#    f.close()

def login_two_factor(): # function used to login to the system
    browser.find_element(By.XPATH, 'XPATH - use CTRL+SHIFT+C to get').send_keys(username)
    otp = simpledialog.askstring(title="OTP",
                                  prompt="Type OTP:")
    otp = password + otp
    browser.find_element(By.XPATH, '//*[@id="inputPassword"]').send_keys(otp)
    captcha = simpledialog.askstring(title="Captcha",
                                  prompt="Type Captcha:")
    browser.find_element(By.XPATH, 'XPATH - use CTRL+SHIFT+C to get').send_keys(captcha)
    browser.find_element(By.XPATH, 'XPATH - use CTRL+SHIFT+C to get').click()

def salva_status(datagram): # function used to save the datagram after full scan, to a .xlsx file
    # create DataFrame using data
    df = pd.DataFrame.from_records(datagram, columns =['REQ','Status REQ', 'WO', 'Status WO', 'TAS', 'Support Group']) # This is the first row of the table
    df.to_excel(file_path+'\status_REQs.xlsx', sheet_name='Status REQ', index=False) # In this case I used a fixed file name, but it can be changed to a variable one

# consulting information
def get_status(req):
    url_search = 'URL_SEARCH'+req # the system uses a URL with a fixed part plus a requisition number
    browser.get(url_search)
    time.sleep(5)
    status_req = browser.find_element(By.XPATH, 'XPATH - use CTRL+SHIFT+C to get')
    status_req = status_req.text
    browser.find_element(By.XPATH, 'XPATH - use CTRL+SHIFT+C to get').click() # I used click to switch between internal pages
    time.sleep(5)
    wo = browser.find_element(By.XPATH, 'XPATH - use CTRL+SHIFT+C to get')
    wo = wo.text
    browser.find_element(By.XPATH, 'XPATH - use CTRL+SHIFT+C to get').click()
    time.sleep(5)
    status_wo = browser.find_element(By.XPATH, 'XPATH - use CTRL+SHIFT+C to get')
    status_wo = status_wo.text
    time.sleep(5)
    try:
        tas = browser.find_element(By.XPATH, 'XPATH - use CTRL+SHIFT+C to get') # this XPATH changes deppending on the REQ status, so I used  a try/except, otherwise I got an not found XPATH error
    except:
        tas = browser.find_element(By.XPATH, 'XPATH - use CTRL+SHIFT+C to get')
    tasclick = tas
    tas = tas.text
    tasclick.click()
    time.sleep(5)
    support_group = browser.find_element(By.XPATH, 'XPATH - use CTRL+SHIFT+C to get')
    support_group = support_group.text
    data = [(req,status_req,wo,status_wo,tas,support_group)]
    return data # return needed to output data value to for loop


# Here is where the program starts
# Open browser and login
browser.get(url)
time.sleep(5)
login_two_factor()
time.sleep(2)

# I used an excel file, which has several REQ values
book = pd.read_excel('excel_file.xlsx', sheet_name='Plan_name')
conteudo = pd.DataFrame(book)

datagram = []
for (row,rs) in conteudo.iterrows():
    req = rs[0]
    data = get_status(req) # getting data variable from get_status function
    datagram += data # each REQ row searched it increments the information on datagram variable
    
save_status(datagram)
pyautogui.alert('Program finished') # Just an alert to know when program finished :)
browser.quit() # close browser
