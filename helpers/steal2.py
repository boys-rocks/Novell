
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from helpers.crop import crop
DRIVER_PATH = 'C:/Users/Thomas/Desktop/Code/chromedriver.exe'
def test_fullpage_screenshot(driver):

    #the element with longest height on page
    ele=driver.find_element("xpath", '//div[@class="container"]')
    total_height = ele.size["height"]+1000
    print(total_height)

    driver.set_window_size(1920, total_height)      #the trick
    time.sleep(2)
    driver.save_screenshot("weathergraphs/top.png")
    driver.execute_script("window.scrollTo(0, 800)")
    driver.save_screenshot("weathergraphs/bottom.png")
    driver.quit()
def getWeatherStats(location,start,end,unit=None):    
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1900")

    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get('https://www.weatherbit.io/history/hourly')
    #print(driver.page_source)
    form = driver.find_elements_by_tag_name('input')
    form[0].send_keys(location)
    if unit == 'c':
        form[2].click()
    form[3].send_keys(start)
    form[4].send_keys(end)
    form[1].click()
    time.sleep(3)
    test_fullpage_screenshot(driver)
    crop("weathergraphs/1.png","weathergraphs/top.png",460,310,1420,680)
    crop("weathergraphs/2.png","weathergraphs/bottom.png",460,70,1420,390)
    crop("weathergraphs/3.png","weathergraphs/bottom.png",460,385,1420,710)
