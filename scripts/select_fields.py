import selenium
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def select_fields(pass_year,semester,driver,class_list,section_number):
  select = Select(driver.find_element_by_id('cbosem'))
  select.select_by_visible_text(str(semester))
  for i in class_list:
    driver.find_element_by_id('txtreg').clear()
    try:
      select = Select(driver.find_element_by_id('txtreg').send_keys(i))
    except AttributeError: 
      pass
    driver.find_element_by_name("Button1").click()
    try:
      print(driver.find_element_by_xpath('//*[@id="lblname"]').text,end=',')
      print(str(section_number),end=',')
      print(i,end=",")
      print(str(pass_year),end=",")
      print(str(semester),end=",")
      print(driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[2]/td[1]').text + " : " + driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[2]/td[4]').text,end=',')
      print(driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[3]/td[1]').text + " : " + driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[3]/td[4]').text,end=',')
      print(driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[4]/td[1]').text + " : " + driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[4]/td[4]').text,end=',')
      print(driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[5]/td[1]').text + " : " + driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[5]/td[4]').text,end=',')
      print(driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[6]/td[1]').text + " : " + driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[6]/td[4]').text,end=',')
      print(driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[7]/td[1]').text + " : " + driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[7]/td[4]').text,end=',')
      print(driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[8]/td[1]').text + " : " + driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[8]/td[4]').text,end=',')
    except:
      pass

    try:
      if(semester == 3 or semester == 4 or semester == 5):
          print(driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[9]/td[1]').text + " : " + driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[9]/td[4]').text,end=',')
          print(driver.find_element_by_xpath('//*[@id="lblgpa"]').text,end=',')
          print(driver.find_element_by_xpath('//*[@id="lblcgpa"]').text,end='\n')
      else:
          print(driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[9]/td[1]').text + " : " + driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[9]/td[4]').text,end=',')
    except:
      pass
    try:
      if (semester == 1 or semester== 2):
      
          print(driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[10]/td[1]').text + " : " + driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[10]/td[4]').text,end=',')
          print(driver.find_element_by_xpath('//*[@id="lblgpa"]').text,end=',')
          print(driver.find_element_by_xpath('//*[@id="lblcgpa"]').text,end='\n')
    except:
        pass
    driver.back()
