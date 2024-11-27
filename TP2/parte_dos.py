def maxCoins( coins ) :
    n = len ( coins )
    dp = [[0] * n for _ in range ( n ) ]
    # length es el núero de monedas en el rango
    for length in range (1 , n +1) :
        for i in range ( n - length + 1) :
            j = i + length - 1 # El final del rango es i + length- 1
            if i == j : # Solo una moneda
                dp [ i ][ j ] = coins [ i ]
            elif i  == j-1:
                dp[i][j] = max(coins[i],coins[j])
            else :
                if coins[i+1]>coins[j]:
                    pick_i = coins[i] + dp[i+2][j]
                else:
                    pick_i = coins[i] + dp[i+1][j-1]
                if coins[j-1]>coins[i]:
                    pick_j = coins[j] + dp[i][j-2]
                else:
                    pick_j = coins[j] + dp[i+1][j-1]
                dp[i][j] = max(pick_i, pick_j)
    return dp[0][n-1]