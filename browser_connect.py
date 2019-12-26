import selenium
import os
def browser_connect():
  # Place path of folder in which GeckoDriver or ChromeDriver resides below
  # os.chdir('.\Folder_Name')
  os.chdir('C:\Drivers\Web_Drivers')
  # For Firefox
  # Change executable_path to where GeckoDriver resides below
  driver = selenium.webdriver.Firefox(executable_path=r'C:\Drivers\Web_Drivers\geckodriver.exe')
  # For Chrome / Chromium
  # Change executable_path to where ChromeDriver resides below
  # driver = selenium.webdriver.Firefox(executable_path=r'C:\Drivers\Web_Drivers\geckodriver.exe')
  # chrome_options = selenium.webdriver.ChromeOptions()
  # driver = selenium.webdriver.Chrome(executable_path=r'C:\Drivers\Web_Drivers\chromedriver.exe',chrome_options=chrome_options)
  driver.get("https://doeresults.gitam.edu/onlineresults/pages/Newgrdcrdinput1.aspx")
  return driver