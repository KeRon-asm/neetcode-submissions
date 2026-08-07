class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> checked;
        for (int i = 0;i<nums.size();i++){
            if (checked.count(nums[i])){
                return true;
            } else{
                checked.insert(nums[i]);
            }
        }
        return false;
    }
};

/*
 checked = []
        for x in nums:
            if x in checked:
                return True
            else:
                checked.append(x)
        return False
*/