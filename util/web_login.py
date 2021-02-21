from util.open_browser import *


def web_login(loginName, password):
    dr = open_browser()
    dr.get('https://cas.leke.cn/login?service=')
    dr.maximize_window()
    dr.find_element_by_id("loginName").send_keys(loginName)
    dr.find_element_by_id("password").send_keys(password)
    dr.find_element_by_id("j-sign-on").click()
    dr.implicitly_wait(5)
    errinfo = dr.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/div[2]/p").text
    dr.quit()
    return errinfo
    # print(errinfo)

