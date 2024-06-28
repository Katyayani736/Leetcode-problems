#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct TreeNode {
  int val;
  TreeNode* left;
  TreeNode* right;
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
  vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
    if (not root) {
      return {};
    }

    vector<vector<int>> ans;
    queue<TreeNode*> q;
    q.push(root);
    int level = 0;
    while (!q.empty()) {
      int size = q.size();
      vector<int> currentLevel(size);
      for (int i = 0; i < size; ++i) {
        TreeNode* node = q.front();
        q.pop();
        currentLevel[i] = node->val;
        if (node->left) {
          q.push(node->left);
        }
        if (node->right) {
          q.push(node->right);
        }
      }

      if (level % 2 == 0) {
        ans.push_back(currentLevel);
      } else {
        reverse(currentLevel.begin(), currentLevel.end());
        ans.push_back(currentLevel);
      }
      level++;
    }

    return ans;
  }
};

// Function to create a binary tree node (helper for user input)
TreeNode* createNode(int data) {
  return new TreeNode(data);
}

int main() {
  cout << "Enter the binary tree structure (level order, space-separated values): ";
  cout << "Enter -1 for null nodes\n";

  int data;
  queue<TreeNode*> q;
  TreeNode* root = nullptr;

  cin >> data;
  if (data != -1) {
    root = createNode(data);
    q.push(root);
  }

  while (!q.empty()) {
    TreeNode* current = q.front();
    q.pop();

    cin >> data;
    if (data != -1) {
      current->left = createNode(data);
      q.push(current->left);
    }

    cin >> data;
    if (data != -1) {
      current->right = createNode(data);
      q.push(current->right);
    }
  }

  Solution solution;
  vector<vector<int>> result = solution.zigzagLevelOrder(root);

  cout << "Zigzag Level Order Traversal: \n";
  for (const vector<int>& level : result) {
    for (int num : level) {
      cout << num << " ";
    }
    cout << endl;
  }

  return 0;
}
