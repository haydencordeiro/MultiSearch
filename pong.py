
import pytest
import time
import json
# from selenium.webdriver.Firefox.options import Options#Firefox  
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options # firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium import webdriver

import tkinter as tk



root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Grocery Help Desk')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter Item Name:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def Sel():

	label3 = tk.Label(root, text= 'Loading The Pages:',font=('helvetica', 10))
	canvas1.create_window(200, 210, window=label3)

	label4 = tk.Label(root, text= 'Have A Great Day',font=('helvetica', 10, 'bold'))
	canvas1.create_window(200, 230, window=label4)
	item=entry1.get()
	driver = webdriver.Firefox()
	links=[]
	driver.get('https://www.amazon.in/s?k={}&ref=nb_sb_noss_2'.format(item))
	links.append('https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'.format(item))
	links.append('https://www.dmart.in/searchResult?searchTerm={}'.format(item))
	links.append('https://www.reliancesmart.in/catalogsearch/result?q={}'.format(item))

	for i in enumerate(links):
	    driver.execute_script("window.open('about:blank', 'tab{}');".format(i[0]))
	    driver.switch_to.window("tab{}".format(i[0]))
	    driver.get(i[1])





    
button1 = tk.Button(text='Open Tabs', command=Sel, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()