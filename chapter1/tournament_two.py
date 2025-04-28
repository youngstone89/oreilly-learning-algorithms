def tournament_two(A):
    N = len(A)
    # initialize winner array to None list to the size of N-1
    winner = [None] * (N - 1)
    loser = [None] * (N - 1)
    # store the index of winning number in the previous round but set it to -1 by default in the beginning
    prior = [-1] * (N - 1)
    idx = 0  # initialize the index for tracking where to store the winners and losers
    print('1 prior={}'.format(prior))
    # round 1, only 4 winners out of 8 numbers could survive
    for i in range(0, N, 2):
        if A[i] < A[i + 1]:
            winner[idx] = A[i + 1]  # winner
            loser[idx] = A[i]  # loser
        else:
            winner[idx] = A[i]  # winner
            loser[idx] = A[i + 1]  # loser
        idx += 1  # increase index
        # for loop ends when we traversed the array with 2 step apart

    m = 0  # track new winner's index which steps up 2
    while idx < N - 1:  # because the index must not go over the given size to store
        # 2nd round of comparison to see if who wins between the first two winners
        if winner[m] < winner[m + 1]:
            winner[idx] = winner[m + 1]
            # store the 2nd round loser to the loser tracking list
            loser[idx] = winner[m]
            prior[idx] = m + 1
        else:
            winner[idx] = winner[m]
            loser[idx] = winner[m + 1]
            prior[idx] = m
        m += 2  # 2 step apart
        idx += 1  # increase index to store winner number
    # while loop ends
    print('2 prior={}'.format(prior))

    # find the largest(which is the winner at the tournament)
    largest = winner[m]

    # set potential second largest number from loser's list
    second = loser[m]

    # update m to previously winning numbers location ( which might be the next largest number because they used to be a winner in a round)
    m = prior[m]
    print('winner={}'.format(winner))
    print('loser={}'.format(loser))

    while m >= 0:
        print('while m={}'.format(m))
        if second < loser[m]:
            second = loser[m]
        m = prior[m]  # keep updating m to previous winner

    return (largest, second)


# N = 8
A = [3, 1, 4, 1, 5, 9, 2, 6]
print('A={}'.format(A))
result = tournament_two(A)
print(result)
