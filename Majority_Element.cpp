class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int e, c=0;
        int n=nums.size();
        for(int i=0;i<n;i++){
            if(c==0)
                e=nums[i];
            if(e==nums[i])
                c++;
            else
                c--;
        }
        return e;
    }
};
