import requests
from bs4 import BeautifulSoup
import csv
import time


start_time = time.time()
url = "https://hoopshype.com/salaries/players/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    tds = soup.find_all('td', {"class": 'name'})[:101]

    with open('bs_players.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Name", "Team", "Position", "Born", "Height", "Weight", "Salary"])

        for td in tds:
            player_link = td.find('a')
            if player_link:
                try:
                    player_url = player_link['href']

                    page = requests.get(player_url)
                    soup = BeautifulSoup(page.content, 'html.parser')

                    name = soup.find('div', {'class': 'player-fullname'})
                    name = name.text.strip() if name else "N/A"

                    team_div = soup.find('div', {'class': 'player-team'})
                    team = team_div.find('a').text.strip() if team_div and team_div.find('a') else "N/A"

                    position = soup.find('span', {'class': 'player-bio-text-line-value'})
                    position = position.text if position else "N/A"

                    born = soup.find_all('span', {'class': 'player-bio-text-line-value'})[1]
                    born = born.text if born else "N/A"

                    height = soup.find_all('span', {'class': 'player-bio-text-line-value'})[2]
                    height = height.text if height else "N/A"

                    weight = soup.find_all('span', {'class': 'player-bio-text-line-value'})[3]
                    weight = weight.text if weight else "N/A"

                    salary = soup.find_all('span', {'class': 'player-bio-text-line-value'})[4]
                    salary = salary.text if salary else "N/A"

                    print("Name :", name)
                    print("Team: ", team)
                    print("Position:", position)
                    print("Born:", born)
                    print("Height:", height)
                    print("Weight:", weight)
                    print("Salary:", salary)
                    print('-----------------------------------------------------')

                    csvwriter.writerow([name, team, position, born, height, weight, salary])

                    end_time = time.time()

                    print("Runtime BeautifulSoup", end_time - start_time)

                except:
                    pass

    print("Player information saved to 'player_info.csv'")

else:
    print("Failed to retrieve the webpage.")
