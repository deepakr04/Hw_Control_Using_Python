import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import sys


def iboot_PDU(url, user_select):
    
    #iboot credentials
    iboot_username = 'admin'
    iboot_pwd = 'admin2a001a'
    
    # Set up the Firefox WebDriver    
    driver = webdriver.Firefox()
    
    driver.maximize_window()
        
    driver.get(url)
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "user-pasword")
    
    username.send_keys(iboot_username)
    password.send_keys(iboot_pwd)
    time.sleep(2)
    
    driver.find_element("xpath", '/html/body/div[2]/div/form/div[5]/div/button').click()
    time.sleep(2)
    
    response = requests.get(driver.current_url)
    
    if user_select == '1':
        print("ON/RECYCLE ALL H/W EQUIPMENTS")
        #pwr_supply
        driver.find_element("xpath", "//*[@id='local-outlet0']").click()
        time.sleep(2)

        #trace_32
        driver.find_element("xpath", "//*[@id='local-outlet1']").click()
        time.sleep(2)

        #outlet_3
        driver.find_element("xpath", "//*[@id='local-outlet2']").click()
        time.sleep(2)

        #Ethernet_3
        driver.find_element("xpath", "//*[@id='local-outlet3']").click()
        time.sleep(2)
        
        #Click ON_BUTTON
        driver.find_element("xpath", "//*[@id='local-controls']/a[1]").click()
        time.sleep(10)
        
    elif user_select == '2':
        print("Turn OFF all the equipment's i.e. all connected: ")
        
        #pwr_supply
        driver.find_element("xpath", "//*[@id='local-outlet0']").click()
        time.sleep(2)

        #trace_32
        driver.find_element("xpath", "//*[@id='local-outlet1']").click()
        time.sleep(2)

        #outlet_3
        driver.find_element("xpath", "//*[@id='local-outlet2']").click()
        time.sleep(2)

        #Ethernet_3
        driver.find_element("xpath", "//*[@id='local-outlet3']").click()
        time.sleep(2)
        
        #Click OFF_BUTTON
        driver.find_element("xpath", "//*[@id='local-controls']/a[2]").click()
        time.sleep(10)
        
        #Log-off and Quit
        driver.find_element("xpath", "//*[@id='profile-dropdown']/li/a").click()
        time.sleep(4)
        
        driver.quit()
        
    elif user_select = '3':
    
        print("Power Cycle all the Equipment's i.e. connected: ")
     
        #pwr_supply
        driver.find_element("xpath", "//*[@id='local-outlet0']").click()
        time.sleep(2)

        #trace_32
        driver.find_element("xpath", "//*[@id='local-outlet1']").click()
        time.sleep(2)

        #outlet_3
        driver.find_element("xpath", "//*[@id='local-outlet2']").click()
        time.sleep(2)

        #Ethernet_3
        driver.find_element("xpath", "//*[@id='local-outlet3']").click()
        time.sleep(2)
        
        #Click Cycle_BUTTON
        driver.find_element("xpath", "//*[@id='local-controls']/a[3]").click()
        time.sleep(10)
    
    
    
    return

def main():

    input_select = True
    
    while input_select:
    
        print(" >>>>>>>>           SELECT ANYONE OF THE BELOW        <<<<<<<<<<")
        print("\n")
        print(" >> PRESS 1 TO ON/RECYCLE ALL H/W EQUIPMENTS << ")
        print("\n")
        print(" >> PRESS 2 TO RESET SELECTED H/W EQUIPMENTS << ")
        print("\n")
        print(" >> PRESS 3 TO DEFAULT TURN OFF ALL THE H/W EQUIPMENTS OF THE STATION << ")
        print("\n")
        print(" >> PRESS 4 TO EXIT FROM AUTOMATING THE H/W << ")
        print("\n")
        
        user_select = input("Press either 1/2/3 only: ")
        
        # Check if the input is equal to "1 or 2 or 3"
        if user_select == '1':
            print("Turn ON all the euqipment's i.e. connected: ")
            input_select = False
        elif user_select == '2':
            print("Tunr OFF all the equipments i.e. connected: ")
            input_select = False
        elif user_select == '3':
            print("Power CYCLE all the equipment's i.e. connected: ")
            input_select = False
        elif user_select == '4':
            print("EXIT FROM AUTOMATING OF THE H/W")
            sys.exit()  # Exit the script
        else:
            print("Check your Input should be either 1/2/3 only")
            continue
    
    # Below Logic will check the response from DMU i.e. iboot PDU ip i.e. 192.168.111.254
    iboot_ip = 'http://192.168.111.254/'
    
    while True:
        response = requests.get(iboot_ip)
        
        if response.status_code == 200:
        
            print('iBoot PDU Request was successful')
            
            iboot_PDU(iboot_ip, user_select)
            
            
        else:
        
            print('Request failed with status code Run and Check Again:', response.status_code)
            
            # Wait for 2 second before sending the next request
            time.sleep(2)
            
            break
    
if __name__ == "__main__":
    main()