from selenium import webdriver
import time

# getting the google form
web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform')
time.sleep(2)

# filling name
name = web.find_element( 'xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys("Niharika")

# filling contact number
contact = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
contact.send_keys("1234567892")

# filling email
email = web.find_element('xpath' , '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
email.send_keys('xyz@gmail.com')

# filling address
address = web.find_element('xpath' , '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
address.send_keys('Delhi')

# filling pincode
pin = web.find_element('xpath' , '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
pin.send_keys('110001')

# filling date of birth
dob_field = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
dob_field.clear()
dob_field.send_keys('23-08-2000')

# filling gender
gender = web.find_element('xpath' , '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
gender.send_keys("female")

#filling secret code
code = web.find_element('xpath' , '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
code.send_keys('GNFPYC')

#submit form
submit_button = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit_button.click()


time.sleep(100)