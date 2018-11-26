import csv

exp_players = []
nov_players = []
Sharks = []
Dragons = []
Raptors = []

def reader():
    with open('soccer_players.csv', newline=' ') as csv_file:
        players = csv.DictReader(csvfile, delimiter=',')
        for player in players:
            if player[2] == 'YES':
                exp_players.append(player)
            if player[2] == 'NO':
                nov_players.append(player)

def divide_teams():
    Sharks.append(exp_players[:3] + nov_players[:3])
    Dragons.append(exp_players[3:6] + nov_players[3:6])
    Raptors.append(exp_players[6:] + nov_players[6:])

def roster(team):
    print(team, '\n', '=' * 10)
    for player in team:
        print(player + '\n')

def roster_list():
    with open('teams.txt', 'a') as file:
        file.write(roster(Sharks), roster(Dragons), roster(Raptors))

def all_together():
    reader(soccer_players.csv)
    divide_teams()
    roster(Sharks)
    roster(Dragons)
    roster(Raptors)
    roster_list()


if __name__ == '__main__':
    all_together()
