import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')

#页面元素的操作
#跳入到内嵌网页中
driver.switch_to.frame('login_frame')               #name或id

#driver.find_element_by_css_selector('#switcher_plogin').click()             #css选择器 id选择器
driver.find_element_by_css_selector('#u').send_keys('306500039')            #css选择器 id选择器
driver.find_element_by_css_selector('#p').send_keys('jason3263164')         #css选择器 id选择器

driver.find_element_by_css_selector('.btn').click()                         #css选择器  class选择器，可能会重复，导致定位失败

time.sleep(1)

#断言
#页面跳转是否正确
#页面信息   桂林山水甲天
resultTitle = driver.title
driver.switch_to.frame('mainFrame')
userText = driver.find_element_by_id('today_alias').text

print('实际的url:',resultTitle)
print('文本信息：',userText)

if resultTitle == 'QQ邮箱' and userText == '桂林山水甲天':
    print('测试通过!')
else:
    print('测试不通过！')

#关闭浏览器
driver.close()
















