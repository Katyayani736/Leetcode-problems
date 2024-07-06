class Solution {
public:
  bool eval(TreeNode* root) {
    if (root->val == 0 || root->val == 1) return root->val == 1;
    else if (root->val == 2) return eval(root->left) || eval(root->right);
    else if (root->val == 3) return eval(root->left) && eval(root->right);
    return false;
  }

  bool evaluateTree(TreeNode* root) {
    return eval(root);
  }

private:
  // Helper function to create tree nodes (optional)
  TreeNode* createNode(int val) {
    return new TreeNode(val);
  }

  // Predefined tree structure (replace with your desired structure)
  TreeNode* root = createNode(2); // Root with value 2 (OR)
  TreeNode* left = createNode(1); // Left child with value 1 (TRUE)
  TreeNode* right = createNode(3); // Right child with value 3 (AND)
                                   //  (can be further expanded)
  right->left = createNode(0);  // Left child of right (FALSE)
  right->right = createNode(1); // Right child of right (TRUE)

  // ... Constructor (optional) to initialize the tree in the object
  Solution() {
    root->left = left;
    root->right = right;
  }
};
