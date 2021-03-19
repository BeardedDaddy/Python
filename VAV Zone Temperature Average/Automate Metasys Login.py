from selenium import webdriver
from getpass import getpass
import subprocess

subprocess.call("")

username_textbox = input("Enter in your username: ")
password = ("Enter in your password: ")

username_textbox = driver.find_element_by_id()
username_textbox.send_keys()

password_textbox = driver.find_element_by_id()
password_textbox.send_keys()

login_button = driver.find_element_by_id()
login_button.submit()
