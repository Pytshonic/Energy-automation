from selenium import webdriver
import time


#might have to download a chrome web driver and use this line to point selenium to the webdriver
driver = webdriver.Chrome("C:\anthony hardrive\DUMP\mid-tempsave")


driver.get("https://energycode.pnl.gov/COMcheckWeb/index.html")
print (driver.title)  


time.sleep(5)
Envelopetab = driver.find_element ("id", 'EnvelopeTab')    
Envelopetab.click() 
print("THIS IS THE TITTLE 1")
   


ext_wall = driver.find_element ("xpath", "/html/body/div[1]/div[5]/form/div[1]/div[2]/div[2]/a[3]")
ext_wall.click()

#run this code to click the radio button
'''
driver.get("https://energycode.pnl.gov/COMcheckWeb/ag_wall.html#ag_wall")
print(driver.title)
Wall_type = driver.find_element ("id", "WOOD_FRAME_16_AG_WALL")
Wall_type.click()
'''
time.sleep(60) 


#create = driver.find_element ("xpath", "/html/body/div[6]/div[3]/div/div/div/div[3]/div/span[1]/button")
#driver.switch_to.frame("")    

'''
print("THIS IS THE TITTLE 2")
A = driver.window_handles
print(A) 
'''





#SWITCH WINDOWS SO COMPUTER LOOKS AT WALL POP UP! 
#HERE'S HOW TO DO IT https://stackoverflow.com/questions/19403949/how-to-handle-pop-up-in-selenium-webdriver-using-java#:~:text=To%20switch%20to%20a%20popup,you%20the%20parent%20window%20itself.&text=Save%20this%20answer.,-Show%20activity%20on

#click ext. Wall tab
#select a wall type (for future add a feature that allows for manual selection, for now just automatically choose 1)
#click create wall button (maybe I can create the whole wall with just this button in the future)
#click area box and input area 

#AO WITH AI ATO WITH AI ATO WITH AI ATO WITH AI 




#this makes sure the browser stays open for 5sec
# do this to make it stay open after running widget
# https://stackoverflow.com/questions/51865300/python-selenium-keep-browser-open
     


#driver.findElement(By.partialLinkText(“”)).click();