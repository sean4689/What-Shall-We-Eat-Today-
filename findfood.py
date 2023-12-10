from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from random import choice
import json
# 透過Browser Driver 開啟 Chrome
def finddata(page,pos):
    name=[]
    # image=[]
    driver = webdriver.Chrome()
    default_url = "https://www.google.com/search?q="+pos+"美食餐廳&sca_esv=583577791&biw=1537&bih=963&tbm=lcl&sxsrf=AM9HkKkgrTBADJZOg_gH4HqGd7uFQFyY3A%3A1700311506922&ei=0rFYZeTuN4qNoATsorfwCw&ved=2ahUKEwjui46K79eCAxXYdPUHHerlCDAQwywoAXoECAUQIg&oq=%E4%B8%AD%E5%8E%9F%E5%95%86%E5%9C%88%E7%BE%8E%E9%A3%9F&gs_lp=Eg1nd3Mtd2l6LWxvY2FsIhLkuK3ljp_llYblnIjnvo7po59IAFAAWABwAHgAkAEAmAEAoAEAqgEAuAEMyAEA&sclient=gws-wiz-local&rlfi=hd:;si:&tbs=lrf:!1m4!1u3!3m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u1!2m2!1m1!1e1!1m4!1u1!2m2!1m1!1e2!1m5!1u2!3m2!2m1!2e8!4e2!2m1!1e2!2m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:9&rlst=f"
    driver.get(default_url)
    for i in range(page):
        element = driver.find_elements(By.XPATH, ("//span[@class='OSrXXb']"))
        # img=driver.find_elements(By.XPATH, ("//img[@class='YQ4gaf zr758c wA1Bge']"))
        # for i in img:
        #     # f.write(i+"\n")
        #     a=i.get_attribute("src")
        #     image.append(a)
        for i in element:
            name.append(i.text)    
        try :
            nextpage=driver.find_element(By.CLASS_NAME,"fl")
            nextpage.click()    
        except:
            print("沒有第二頁")
        time.sleep(2)        
    driver.close()
    # conbine=dict(zip(name,image))
    # return conbine
    return name
# def wwrite(c=dict):
#       with open('food.json', 'w') as file:
#         file.write(json.dumps(c))
def suffer(name):
    return choice(name)

