from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

start_time = time.time()
def scrape_data(driver, link, csv_writer):
    try:
        driver.get(link)
        time.sleep(1)
        
        name = driver.find_element(By.XPATH, '//div[@class="player-fullname"]').text
        team = driver.find_element(By.XPATH, '//div[@class="player-team"]/a').text
        
        position = driver.find_element(By.XPATH, '//span[@class="player-bio-text-line"]/b[text()="Position:"]/following-sibling::span').text
        born = driver.find_element(By.XPATH, '//span[@class="player-bio-text-line"]/b[text()="Born:"]/following-sibling::span').text
        height = driver.find_element(By.XPATH, '//span[@class="player-bio-text-line"]/b[text()="Height:"]/following-sibling::span').text
        weight = driver.find_element(By.XPATH, '//span[@class="player-bio-text-line"]/b[text()="Weight:"]/following-sibling::span').text
        salary = driver.find_element(By.XPATH, '//span[@class="player-bio-text-line"]/b[text()="Salary:"]/following-sibling::span').text
        
        data = [name, team, position, born, height, weight, salary]
        csv_writer.writerow(data)
        
        print("Name:", name)
        print("Team:", team)
        print("Position:", position)
        print("Born:", born)
        print("Height:", height)
        print("Weight:", weight)
        print("Salary:", salary)
        print("--------------------------------")
    except:
        pass

driver = webdriver.Chrome()
driver.get("https://hoopshype.com/salaries/players/")
time.sleep(2)

player_links = driver.find_elements(By.XPATH, '//td[@class="name"]/a')[:101]
links = [link.get_attribute("href") for link in player_links]

with open('selenium_players.csv', mode='w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Name', 'Team', 'Position', 'Born', 'Height', 'Weight', 'Salary'])
    
    for link in links:
        scrape_data(driver, link, csv_writer)


end_time = time.time()

driver.quit()

print("Runtime Selenium", end_time - start_time)