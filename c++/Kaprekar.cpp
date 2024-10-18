#include <iostream>

// Definition for a binary tree node
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// Pre-order traversal of the tree
void preOrderTraversal(TreeNode* root) {
    if (root == nullptr) {
        return;
    }

    // Visit the current node
    std::cout << root->val << " ";

    // Traverse the left subtree
    preOrderTraversal(root->left);

    // Traverse the right subtree
    preOrderTraversal(root->right);
}

// Helper function to delete the tree and free memory
void deleteTree(TreeNode* root) {
    if (root == nullptr) {
        return;
    }

    // Recursively delete the left and right subtrees
    deleteTree(root->left);
    deleteTree(root->right);

    // Delete the current node
    delete root;
}

int main() {
    // Create a sample binary tree
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    // Perform pre-order traversal
    std::cout << "Pre-Order Traversal: ";
    preOrderTraversal(root);
    std::cout << std::endl;

    // Clean up memory by deleting the tree
    deleteTree(root);

    return 0;
}
