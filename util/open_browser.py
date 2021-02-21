from selenium import webdriver


def open_browser():
    dr = webdriver.Chrome('../tools/chromedriver.exe')
    return dr
