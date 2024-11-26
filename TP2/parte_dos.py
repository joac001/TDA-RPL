def maxCoins(coins):
    n = len(coins)
    dp = [[0] * n for _ in range(n)]
    
    # Llenar la tabla diagonalmente
    for length in range(1, n+1):  # length es el número de monedas en el rango
        for i in range(n - length + 1):
            j = i + length - 1  # El final del rango es i + length - 1
            
            # Si sólo queda una moneda
            if i == j:
                dp[i][j] = coins[i]
            else:
                # Elegir entre la primera o la última moneda
                pick_i = coins[i] + min(dp[i+2][j] if i+2 <= j else 0, dp[i+1][j-1] if i+1 <= j-1 else 0)
                pick_j = coins[j] + min(dp[i+1][j-1] if i+1 <= j-1 else 0, dp[i][j-2] if i <= j-2 else 0)
                
                dp[i][j] = max(pick_i, pick_j)
    
    # El valor óptimo para Sophia estará en dp[0][n-1]
    return dp[0][n-1]