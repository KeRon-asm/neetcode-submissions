class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        int minimum_purchase = prices[0];

        for (int& sell : prices) {
            max_profit = max(max_profit, sell - minimum_purchase);
            minimum_purchase = min(minimum_purchase, sell);
        }
        return max_profit;
    }
};
