import requests
import string_cleaner
from selenium import webdriver
import pandas as pd

#chave API AIzaSyCpMCAkuN89MgGDQAxVJfBGcbGA8bosKZQ
#URL Padrão: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY
#minha URL https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyCpMCAkuN89MgGDQAxVJfBGcbGA8bosKZQ

class Finder:
    def __init__(self, url):
        # Setting base url
        self.base_url = url
        
        # Creating driver
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\giu_2\Desktop\DEV\Configurações\chromedriver.exe')
        
        # Initializing in main cartola data page
        self.driver.get(self.base_url)


a = string_cleaner.Cleaner()
a.set_url_params()
c = Finder(a.url)
c.driver.get
b = pd.read_json(a.url)
d = b['results']
print(d)