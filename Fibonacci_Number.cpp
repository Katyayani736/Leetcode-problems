//Using dynamic programming and space optimization.
#include <iostream>

class Solution {
public:
  int fib(int n) {
    if (n <= 1) {
      return n;
    }

    int p2 = 0;  // Previous second Fibonacci number
    int p = 1;   // Previous Fibonacci number
    int sum = 0;  // Current Fibonacci number

    for (int i = 2; i <= n; i++) {
      sum = p2 + p;
      p2 = p;
      p = sum;
    }

    return p;
  }
};

int main() {
  int n;

  std::cout << "Enter the index of the Fibonacci number (0-based): ";
  std::cin >> n;

  Solution solution;
  int result = solution.fib(n);

  std::cout << "The " << n << "th Fibonacci number is: " << result << std::endl;

  return 0;
}
