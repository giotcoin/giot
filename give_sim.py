print "Compute gives for validators and delegators over time"
import math

givesVal = 0.000    # starting gives for validator
givesDel = 0.010    # starting gives delegated to validator
givesAll = 1.0      #
inflation = 0.3     # 30% inflation
inflationLg = math.log(1.0 + inflation) # for exponential
exponential = True  # exponential
commission = 0.10   # 5% commission
numBlocksPerYear = 1000


for year in range(0,50):
  rewardsYear = 0.0
  for i in range(0,numBlocksPerYear):
    if exponential:
      blockReward = (givesAll * inflationLg) / float(numBlocksPerYear)
    else:
      blockReward = inflation / float(numBlocksPerYear)

    givesAll += blockReward
    rewardsYear += blockReward
    rewardVal = blockReward * (givesVal / givesAll)
    rewardDel = blockReward * (givesDel / givesAll)
    rewardVal += rewardDel * commission
    rewardDel *= (1.0 - commission)
    givesVal += rewardVal
    givesDel += rewardDel
    #print givesVal, givesDel, (givesVal / givesAll)
  print year, "givesVal: %0.3f" % (givesVal,), "givesDel: %0.3f" % (givesDel,), \
  "givesAll: %0.3f" % (givesAll,), "givesVal%%: %0.2f" % ((100 * givesVal / givesAll),), \
  "givesDel%%: %0.2f" % ((100 * givesDel / givesAll),), "rewards: %0.2f"%(rewardsYear,), \
  "valDelRatio: %0.3f" % (givesVal / (givesDel + givesVal))
