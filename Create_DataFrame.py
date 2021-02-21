import Coin_Problem as CP
import collections
import pandas as pd
import numpy as np


def probability_dataframe(iterations):

    probability_box1 = np.empty([iterations, 1])
    probability_box2 = np.empty([iterations, 1])
    probability_box3 = np.empty([iterations, 1])
    probability_firstcoin_gold = np.empty([iterations, 1])
    probability_firstcoin_silver = np.empty([iterations, 1])
    probability_secondcoin_gold = np.empty([iterations, 1])
    probability_secondcoin_silver = np.empty([iterations, 1])
    probability_paradox_gold = np.empty([iterations, 1])
    probability_paradox_silver = np.empty([iterations, 1])

    for k in range(1, iterations + 1):

        coin_and_box_list = CP.Bertrand_Box_Paradox(k)
        # [firstcoinpull, secondcoinpull, box1counter, box2counter, box3counter]

        probability_box1[k - 1, 0] = coin_and_box_list[2] / k
        probability_box2[k - 1, 0] = coin_and_box_list[3] / k
        probability_box3[k - 1, 0] = coin_and_box_list[4] / k
        probability_firstcoin_gold[k - 1, 0] = collections.Counter(coin_and_box_list[0])['Gold'] / k
        probability_firstcoin_silver[k - 1, 0] = collections.Counter(coin_and_box_list[0])['Silver'] / k
        probability_secondcoin_gold[k - 1, 0] = collections.Counter(coin_and_box_list[1])['Gold'] / k
        probability_secondcoin_silver[k - 1, 0] = collections.Counter(coin_and_box_list[1])['Silver'] / k

        total_firstcoin_goldset = len([(i, j) for i, j in zip(coin_and_box_list[0], coin_and_box_list[1])
                                       if i == 'Gold'])
        total_firstcoin_silverset = len([(i, j) for i, j in zip(coin_and_box_list[0], coin_and_box_list[1])
                                         if i == 'Silver'])

        if total_firstcoin_goldset == 0 or total_firstcoin_silverset == 0:
            probability_paradox_gold[k - 1, 0] = \
                len([(i, j) for i, j in zip(coin_and_box_list[0], coin_and_box_list[1])
                     if i == 'Gold' and j == 'Gold']) / k

            probability_paradox_silver[k - 1, 0] = \
                len([(i, j) for i, j in zip(coin_and_box_list[0], coin_and_box_list[1])
                     if i == 'Silver' and j == 'Silver']) / k

        else:
            probability_paradox_gold[k - 1, 0] = \
                len([(i, j) for i, j in zip(coin_and_box_list[0], coin_and_box_list[1])
                     if i == 'Gold' and j == 'Gold']) / total_firstcoin_goldset

            probability_paradox_silver[k - 1, 0] = \
                len([(i, j) for i, j in zip(coin_and_box_list[0], coin_and_box_list[1])
                     if i == 'Silver' and j == 'Silver']) / total_firstcoin_silverset

    graphing_data = pd.DataFrame({'Box 1': probability_box1[:, 0],
                                  'Box 2': probability_box2[:, 0],
                                  'Box 3': probability_box3[:, 0],
                                  'First Coin: Gold': probability_firstcoin_gold[:, 0],
                                  'First Coin: Silver': probability_firstcoin_silver[:, 0],
                                  'Second Coin: Gold': probability_secondcoin_gold[:, 0],
                                  'Second Coin: Silver': probability_secondcoin_silver[:, 0],
                                  'Gold': probability_paradox_gold[:, 0],
                                  'Silver': probability_paradox_silver[:, 0]})

    return graphing_data
