class Solution {
public:
    int func(int r1,int c1,int r2,int n,vector<vector<int>>& grid,vector<vector<vector<int>>> &dp){
        int c2=r1+c1-r2;
        if(r1>=n or c1>=n or r2>=n or c2>=n or grid[r1][c1]==-1 or grid[r2][c2]==-1)
            return -1e9;
        if(dp[r1][c1][r2]!=-1)
            return dp[r1][c1][r2];
        if(r1==n-1 and c1==n-1) return grid[r1][c1];
        int temp=0;
        if(r1==r2 and c1==c2)
            temp+=grid[r1][c1];
        else temp+=grid[r1][c1] + grid[r2][c2];

        int a=func(r1+1,c1,r2+1,n,grid,dp);
        int b=func(r1+1,c1,r2,n,grid,dp);
        int c=func(r1,c1+1,r2+1,n,grid,dp);
        int d=func(r1,c1+1,r2,n,grid,dp);

        temp+=max({a,b,c,d});
        dp[r1][c1][r2]=temp;
        return temp;
    }
    int cherryPickup(vector<vector<int>>& grid) {
        int n=grid.size();
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(n, vector<int>(n,-1)));
        return max(0,func(0,0,0,n,grid,dp));
    }
};
