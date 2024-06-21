class Solution {
public:
    int climbStairs(int n) {
        int p2=1;
        int p=1;
        int sum=0;
        for (int i=2;i<=n;i++){
            sum=p2+p;
            p2=p;
            p=sum;
        }
        return p;
    }
};
int main() {
    int numStairs;
    cout << "Enter the number of stairs: ";
    cin >> numStairs;
    Solution solution;
    int ways = solution.climbStairs(numStairs);
    cout << "Number of ways to climb " << numStairs << " stairs: " << ways << endl;
    return 0;
}
