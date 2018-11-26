import csv

exp_players = []
nov_players = []

def read_and_divide(info):
    # Function to read csv file and split players based on experience
    with open(info, newline=' ') as csvfile:
        players = csv.DictReader(csvfile, delimiter=',')
        for player in players:
            if player['Soccer Experience'] == 'YES':
                exp_players.append(player)
            else:
                nov_players.append(player)

def roster():
    # Function to equally assign players to teams and print out roster
    sharks = exp_players[:3] + nov_players[:3]
    dragons = exp_players[3:6] + nov_players[3:6]
    raptors = exp_players[6:] + nov_players[6:]
    every_team = {'Sharks': sharks, 'Dragons': dragons, 'Raptors': raptors}
    with open('teams.txt', 'w') as new_file:
        for name, team in every_team.items():
            new_file.write('\n{}\n'.format(name))
            new_file.write('-' * 10)
            for player in team:
                new_file.write('\n{}\n'.format(player['Name']))
        
def all_together():
    # Function to combine previous two functions
    read_and_divide('soccer_players.csv')
    roster()
        
if __name__ == '__main__':
    # Main logic work
    all_together()
