# -*- coding: UTF-8 -*-

def f(numOfMin, effciency, voteInFavours):
    party_1 = []
    party_2 = []
    for i in voteInFavours:
        if i[0] not in party_1 and i[0] not in party_2:
            party_1.append(i[0])
            party_2.append(i[1])
        else:
            if i[0] not in party_2:
                party_2.append(i[1])
            else:
                party_1.append(i[1])

    ef_1 = [effciency[i-1] for i in party_1]
    ef_2 = [effciency[i-1] for i in party_2]
    score_1 = sum(ef_1)
    score_2 = sum(ef_2)
    return max(score_1, score_2)


numOfMin = 7
effciency = [15, 27, 42, 40, 22, 30, 11]
voteInFavours = [[1, 2], [1, 3], [1, 4], [2, 5], [3, 6], [4, 7]]
score = f(numOfMin, effciency, voteInFavours)
print score