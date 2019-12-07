def printknapSack(W, wt, val, n): 
    K = [[0 for w in range(W + 1)] 
            for i in range(n + 1)] 
              
    # Build table K[][] in bottom 
    # up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i - 1] <= w: 
                K[i][w] = max(val[i - 1]  
                  + K[i - 1][w - wt[i - 1]], 
                               K[i - 1][w]) 
            else: 
                K[i][w] = K[i - 1][w] 
  
    # stores the result of Knapsack 
    res = K[n][W]
    final = res
    cards = 0
    w = W 
    for i in range(n, 0, -1): 
        if res <= 0: 
            break
        # either the result comes from the 
        # top (K[i-1][w]) or from (val[i-1] 
        # + K[i-1] [w-wt[i-1]]) as in Knapsack 
        # table. If it comes from the latter 
        # one/ it means the item is included. 
        if res == K[i - 1][w]: 
            continue
        else: 
  
            # This item is included. 
            cards+=1
              
            # Since this weight is included 
            # its value is deducted 
            res = res - val[i - 1] 
            w = w - wt[i - 1] 
    return final,cards
final = 0
cards_now = 0
for turn in range(int(input())):
    wt=[]
    val=[]
    for c in range(int(input())):
        weight,value = map(int,input().split(' '))
        print("YO",weight,value)
        wt.append(weight)
        val.append(val)
    total,cards = printknapSack(3,wt,val,len(wt))
    cards_now+=cards
    if cards_now==10:
        cards_now=0
        final+=2*total
    else:
        final+=total

    
