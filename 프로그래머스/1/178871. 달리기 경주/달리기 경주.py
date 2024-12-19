def solution(players, callings):
    dict = {}
    for index, data in enumerate(players):
        dict[data] = index
    
    for call in callings:
        index = dict[call]
        dict[players[index-1]] = index
        players[index], players[index-1] = players[index-1], players[index]
        dict[call] = index - 1
        
    return players