#include <iostream>
using namespace std;

struct Node{
    int data;
    Node* next;
};

void append(Node*& head, int data){
    // Append data at the end of the link list.
    Node* newNode = new Node{data, nullptr};
    if (head == nullptr){
        head = newNode;
    }else{
        Node* current = head;
        while(current->next != nullptr){
            current = current->next;
        }
        current->next = newNode;
    }
}

void display(Node*& head){
    // Display out the link list, If list was empty, just print "null".
    if (head != nullptr){
        Node* current = head;
        while(current != nullptr){
            cout << current->data << " -> ";
            current = current->next;
        }
    }
    cout << "null" << endl;
}

void deleteNode(Node*& head, int value){
    // Delete a first node with the given value if the node exists.
    if(head != nullptr){
        Node* current = head;
        Node* previous = nullptr;
        while(current != nullptr){
            if(current->data == value){
                if(previous == nullptr){
                    head = current->next;
                }else{
                    previous->next = current->next;
                }
                delete current;
                break;
            }
            previous = current;
            current = current->next;
        }
    }
}

void deleteList(Node*& head){
    // Empty the list and delete all nodes
    while(head != nullptr){
        Node* temp = head;
        head = head->next;
        delete temp;
    }
}

int main(){
    // You can change this section to have you own example

    Node* head = nullptr;
    append(head, 1);
    append(head, 2);
    append(head, 3);
    display(head);
    deleteNode(head, 2);
    display(head);
    deleteList(head);
    display(head);
    
    return 0;
}