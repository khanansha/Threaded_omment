def distribute_coins():
  thief = 3
  coins = 7

  have_coins = 0;
  for i in range(1, thief+1):
    # print(i)
    have_coins = have_coins+i-1;
    # print(have_coins)
    if i == thief:
      remaining_coins = coins-have_coins
      print("Thief "+str(i)+" will have "+str(remaining_coins)+" gold coins.")
    else:
      print("Thief "+str(i)+" will have "+str(i)+" gold coins.")
      
    
distribute_coins()
