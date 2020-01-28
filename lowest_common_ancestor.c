#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

struct node {
    
    int data;
    struct node *left;
    struct node *right;
  
};

struct node* insert( struct node* root, int data ) {
		
	if(root == NULL) {
	
        struct node* node = (struct node*)malloc(sizeof(struct node));

        node->data = data;

        node->left = NULL;
        node->right = NULL;
        return node;
	  
	} else {
      
		struct node* cur;
		
		if(data <= root->data) {
            cur = insert(root->left, data);
            root->left = cur;
		} else {
            cur = insert(root->right, data);
            root->right = cur;
		}
	
		return root;
	}
}

/* you only have to complete the function given below.  
node is defined as  

struct node {
    
    int data;
    struct node *left;
    struct node *right;
  
};

*/

int findInBST(struct node *root, int v) {
    if (root == NULL){
        return 0;
    } else if (root->data == v) {
        return 1;
    } else if (root->data > v) {
        return findInBST(root->left, v);
    } else {
        return findInBST(root->right, v);
    }
}
struct node *lca( struct node *root, int v1, int v2 ) {
    int lf = 0;
    int rf = 0;
    if ((root->data == v1) || (root->data == v2)) {
        return root;
    }
    lf = findInBST(root->left, v1);
    rf = findInBST(root->right, v2);

    if (lf == rf) {
        return root;
    } else if (lf == 0 && rf == 1){
        return lca(root->right, v1, v2);
    } else {
        return lca(root->left, v1, v2);
    }
}


int main() {
  
    struct node* root = NULL;
    
    int t;
    int data;

    scanf("%d", &t);

    while(t-- > 0) {
        scanf("%d", &data);
        root = insert(root, data);
    }
  	int v1;
  	int v2;
  
  	scanf("%d%d", &v1, &v2);
	struct node *ans = lca(root, v1, v2);
  	printf("%d", ans->data);
  	
    return 0;
}
