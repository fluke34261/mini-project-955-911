from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge('/Users/chaloemphonthipkasorn/msedgedriver')

# url = "https://nbia.cancerimagingarchive.net/nbia-viewer/?thumbnailSeries=5079045&thumbnailDescription=T2%20TSE%20ax%20hi&accessToken=565c3fd0-3b3f-4a0e-b833-426163baec3d:7af7cdca-9a27-41de-90d2-c26e74ade608:6798"
url = "https://nbia.cancerimagingarchive.net/nbia-search/"
driver.get(url)

try:
    element = WebDriverWait(driver, 60).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "loading-div"))
    )
finally:
    driver.find_element(By.XPATH, "/html/body/nbia-root/nbia-nbia-client/nbia-introduction/div/div[2]/span/div[2]/button[3]").click()
    driver.implicitly_wait(5) # seconds
    
    driver.find_element(By.XPATH, "/html/body/nbia-root/nbia-nbia-client/div/nbia-image-search/div/div[1]/nbia-query-section/div/nbia-query-section-tabs/nbia-simple-search/div/nbia-collection-query/div/div[1]/label").click()
    driver.implicitly_wait(3) # seconds
    

    driver.find_element(By.XPATH, "//input[@id=\"collectionsSearchText\"]").send_keys("PROSTATE-MRI")
    driver.find_element(By.XPATH, "//input[@id=\"collectionsSearchText\"]").send_keys(Keys.RETURN)
    
    driver.find_element(By.XPATH, "/html/body/nbia-root/nbia-nbia-client/div/nbia-image-search/div/div[1]/nbia-query-section/div/nbia-query-section-tabs/nbia-simple-search/div/nbia-collection-query/div/div[2]/div[2]/div[2]/span/label[1]").click()
    driver.find_element(By.XPATH, "/html/body/nbia-root/nbia-nbia-client/div/nbia-image-search/div/div[2]/nbia-data-section/div/nbia-data-section-tabs/span/ul/li[2]/span").click()
    # driver.implicitly_wait(10) # seconds

    driver.find_element(By.XPATH, "//a[contains(text(),'MIP-PROSTATE-01-0001')]").click();
    driver.implicitly_wait(3) # seconds
    driver.find_element(By.XPATH, "//a[contains(text(),'Apr 30, 2006')]").click();

    driver.find_element(By.XPATH, "/html/body/nbia-root/nbia-nbia-client/div/nbia-image-search/div/div[2]/nbia-data-section/div/nbia-data-section-tabs/nbia-search-results/div/div[2]/nbia-search-results-table/div/table/tr[3]/td/nbia-subject-study-details/div/div/div/span/nbia-series-details/table/tr[10]/td[7]/label[1]").click();
    
    # driver.close()

    
