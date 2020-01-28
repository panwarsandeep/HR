/* Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may want to write one or more helper functions.  

The Node struct is defined as follows:
	struct Node {
		int data;
		Node* left;
		Node* right;
	}
*/

bool checkMaxMin(Node* root, int val, bool is_max) {
    if (root == NULL) {
        return true;
    } else if (((root->data >= val) && is_max ) ||
               ((root->data <= val) && !is_max) ){
        return false;
    } else {
        return (checkMaxMin(root->left, val, is_max) && 
                checkMaxMin(root->right, val, is_max));
    }
}
	bool checkBST(Node* root) {
		if (root == NULL) {
            return true;
        } else if (checkMaxMin(root->left, root->data, true) && checkMaxMin(root->right, root->data, false)) {
            return (checkBST(root->left) && checkBST(root->right));
        } else {
            return false;
        }
	}