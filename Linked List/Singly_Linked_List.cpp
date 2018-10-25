/*
** This CODE can be written using class
** i.e. OOP (Object Oriented Programming).
** Even the OOP CODE is more manageable.
** But the of OOP has not been used for
** the simplicity of understanding.
*/


/************************
** MAHMOOD AL RAYHAN   **
** All Rights Reserved **
************************/


#include<iostream>
#include<cstdio>
using namespace std;


/// The memory block structure
struct node
{
    int value;
    struct node *next;
};


/// Global variables
node *head, *tail, *access;
int number_of_node;


/// Initializes all the Global variables
void initialize()
{
    head = new node, head = NULL;
    tail = new node, tail = NULL;
    access = new node, access = NULL;
    number_of_node = 0;
}


/// This function always resets
/// the access pointer to head
void reset_access()
{
    access = head;
}


/// Check with this function before removing or popping
/// element that, whether the list is already empty or not.
bool is_emply()
{
    return number_of_node;
}


/// This function searches the nth node
/// from the start of the list
int search_nth_node(int node_number, bool reset)
{
    if(node_number > number_of_node)
        return -1;

    access = head;
    int nv;

    int c = 0;
    while(access != NULL)
    {
        c++;
        if(c == node_number)
        {
            nv = access->value;
            if(reset)
                reset_access();
            return nv;
        }
        access = access->next;
    }
}


/// This function adds a new
/// node at the front of list.
void push_node_to_front(int v)
{
    node *new_node = new node;

    new_node->value = v;
    new_node->next = head;

    head = new_node;

    number_of_node++;
    reset_access();
}


/// This function adds a new
/// node at the end of list.
void push_node_to_back(int v)
{
    node *new_node = new node;
    new_node->value = v;

    if(number_of_node != 0)
    {
        new_node->next = NULL;
        tail->next = new_node;
        tail = tail->next;
    }
    else
    {
        head = tail = new_node;
        head->next = tail->next = NULL;
    }

    number_of_node++;
}


/// Pop and return a node from front
int pop_node_from_front()
{
    int nv = head->value;
    head = head->next;
    number_of_node--;
    if(number_of_node == 0)
        initialize();
    reset_access();
    return nv;
}


/// Pop and return a node from back
int pop_node_from_back()
{
    access = head;
    int nv;

    if(access->next == NULL)
    {
        nv = access->value;
        initialize();
        return nv;
    }

    while(access->next->next != NULL)
        access = access->next;

    nv = access->next->value;
    access->next = NULL;
    number_of_node--;

    return nv;
}

/// Insert v in position pos
void insert_at_position(int pos, int v)
{
    if(pos <= number_of_node)
    {
        if(pos == 1)
            push_node_to_front(v);
        else
        {
            node *new_node = new node;
            search_nth_node(pos-1, false);

            new_node->next = access->next;
            new_node->value = v;
            access->next = new_node;

        }

        reset_access();
    }
    else
        return;
}


/// Remove node from specified pos
int remove_from_position(int pos)
{
    if(pos <= number_of_node)
    {
        int nv;
        if(pos == 1)
        {
            nv = pop_node_from_front();

            return nv;
        }
        else
        {
            search_nth_node(pos-1, false);
            nv = access->next->value;
            access->next = access->next->next;
            reset_access();
            return nv;
        }
    }
    else
        return;
}


/// Update value of node at pos
void update_value_at_position(int pos, int v)
{
    if(pos <= number_of_node)
    {
        search_nth_node(pos, false);
        access->value = v;
        reset_access();

    }
    else
        return;
}



/// This function print the values
/// in the node of Linked List.
void print_node()
{
    access = head;

    int c = 1;
    while(access != NULL)
    {
        cout<<"Node "<<c<<": "<<access->value<<endl;
        access = access->next;
        c++;
    }

    reset_access();
}




/************************ MAIN FUNCTION ***********************/



int main()
{
//    freopen("in.txt", "r", stdin);

    int n, val, pos;

    initialize();

    cout<<"How many node you want to create? ";
    cin>>n;

    /// Creating the Linked List
    for(int i=0; i<n; i++)
    {
        cin>>val;
        push_node_to_back(val);
    }


    /// TODO do some simulation to play with LINKED LIST


    /**** This is demo playground
    
    print_node();
    cout<<"\n\n";

    cout<<remove_from_position(3)<<endl;
    print_node();
    cout<<"\n\n";

    insert_at_position(1, 3333);
    print_node();
    cout<<"\n\n";

    update_value_at_position(5, 4444);
    print_node();
    cout<<"\n\n";
    
    */


    return 0;
}

