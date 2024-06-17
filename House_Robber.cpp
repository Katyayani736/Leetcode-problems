
#include <bits/stdc++.h>
using namespace std;
int rob(vector<int>& nums) {
    int n=nums.size();
    int p2=0;
    int p=nums[0];
    int curr,pick,notpick;
    for (int i=1;i<n;i++){
        pick=nums[i];
        if(i>1)
            pick=pick+p2;
        notpick=0+p;
        curr=max(pick,notpick);
        p2=p;
        p=curr;
    }
    return p;
}

int main() {
    vector<int> arr{1,2,3,1};
    int n = arr.size();
    cout << solve(n, arr);
    return 0;
}

