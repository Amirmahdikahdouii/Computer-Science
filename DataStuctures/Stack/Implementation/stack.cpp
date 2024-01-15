#include <iostream>
using namespace std;

struct Node
{
    string data;
    Node *next;
};

void push(Node*& top, string data){
    // Create & Append nodes into stack with given data

    Node* new_node = new Node{data, nullptr};
    new_node->next = top;
    top = new_node;
}

string peek(Node*& top){
    // Return top node value

    if (top != nullptr){
        return top->data;
    }
    return "null";
}

string pop(Node*& top){
    /*
    This function will remove top node and return the data.
    If stack was empty, return null.
    */
    if (top != nullptr){
        string data = top->data;
        Node* temp = top;
        top = top->next;
        delete temp;
        return data;
    }
    return "null";
}

void clear(Node*& top){
    /*
    This method will remove all nodes from stack and make it empty.
    */
    while (top != nullptr){
        Node* temp = top;
        top = top->next;
        delete temp;
    }
}

void display(Node*& top){
    /* 
    Print stack node data in console
    If stack was empty just cout null 
    */

    Node* node = top;
    while (node != nullptr){
        cout << node->data << " -> ";    
        node = node->next;
    }
    cout << "null" << endl;
}

int main(){
    // Put Codes in here
    // ...

    return 0;
}