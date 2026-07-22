class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        /*
                n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n-1] = 1
        for i in range(1, n):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range(n-2,-1,-1):
            suff[i] = nums[i+1] * suff[i+1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res

        
        */
        int n    = nums.size();
        vector<int> res(n,1);
        
        for (int i = 1; i < n; i++){
            res[i] = res[i-1] * nums[i-1];
        }
        int postfix = 1;
        for (int i = n-1; i>=0; i--){
            res[i] *= postfix;
            postfix *= nums[i];
        }
        return res;
    }
};
