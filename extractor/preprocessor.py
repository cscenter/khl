# encoding: utf-8

import csv

events_file_name = 'khl_items.csv' # имя файла, содержащего информацию по всем матчам
teams_file_name = 'khl_teams.csv'  # имя файла, в котором будет информация о командах, встречающихся в events_file_name

# порядок всех атрибутов строго задан в пауке
id_num = 0
team1_name_num = 2
team2_name_num = 3

def main():
    print('Started reading events...')

    teams = set()
    with open(events_file_name, newline='', encoding='utf-8') as csvfile:
        khlreader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
        rows = []
        for row in khlreader:
            if row[id_num] != 'id':
                rows.append(row)
                teams.add(row[team1_name_num])
                teams.add(row[team2_name_num])

    print('Finished reading events...')

    print('Processing teams...')
    teams_list = []
    for team in teams:
        teams_list.append(team)
    teams_list.sort()
    id = 1
    teamById = {}
    idByTeam = {}
    # Кунь Лунь в прошлом году не существовало
    # однако если мы хотим в будущем использовать
    # результаты 2015-2016 в текущем сезоне(2016-2017)
    # то добавляет её
    for team in teams_list:
        if (team > 'Йокерит' and team < 'Локомотив'):
            teamById[id] = 'Куньлунь РС'
            idByTeam['Куньлунь РС'] = id
            id += 1
        teamById[id] = team
        idByTeam[team] = id
        id += 1
    with open(teams_file_name, 'w') as csvfile:
        teamswriter = csv.writer(csvfile, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
        for teamId, teamName in teamById.items():
            teamswriter.writerow([teamId, teamName])
    print('Processing teams has done')

if __name__ == '__main__':
    main()