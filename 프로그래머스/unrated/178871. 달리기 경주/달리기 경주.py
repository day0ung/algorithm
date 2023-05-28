def solution(players, callings):
    player_dic = {player: index for index, player in enumerate(players)}

    for call in callings:
        index = player_dic[call]
        player_dic[players[index - 1]],  player_dic[players[index]] = index, index -1
        players[index - 1], players[index] = players[index], players[index - 1]
    return players