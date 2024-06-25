#include <iostream>
#include <vector>
#include <limits>

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n=coins.size();
        vector<int> dp(amount+1,1e7);
        dp[0]=0;
        for(int sum=1;sum<=amount;sum++){
            for(int j=0;j<n;j++){
                if(sum-coins[j]>=0)
                    dp[sum]=min(dp[sum] , dp[sum-coins[j]]+1 );
            }
        }

        return dp[amount]==1e7? -1 : dp[amount];
    }
};

int main() {
    int n, amount;
    std::cout << "Enter the number of coin denominations: ";
    std::cin >> n;

    std::vector<int> coins(n);
    std::cout << "Enter the denominations (separated by spaces): ";
    for (int i = 0; i < n; ++i) {
        std::cin >> coins[i];
    }

    std::cout << "Enter the target amount: ";
    std::cin >> amount;

    Solution solution;
    int minCoins = solution.coinChange(coins, amount);

    if (minCoins == -1) {
        std::cout << "The target amount cannot be formed using the given coins." << std::endl;
    } else {
        std::cout << "Minimum number of coins required: " << minCoins << std::endl;
    }

    return 0;
}
