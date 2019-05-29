#include<bits/stdc++.h>
using namespace std;


int binary_knapsack(int weight[], int profit[], int items, int sack_size)
{
    int board[items+1][sack_size+1];
    int marker[items+1][sack_size+1];

    for(int i=0; i<=items; i++)
    {
        for(int capacity=0; capacity<=sack_size; capacity++)
        {
            if(i==0 or capacity==0)
                board[i][capacity] = 0 /**, marker[i][capacity] = 0*/;
            else if(weight[i-1] > capacity)
                board[i][capacity] = board[i-1][capacity] /**, marker[i][capacity] = 0*/;
            else
            {
                board[i][capacity] = max(
                                         profit[i-1]+board[i-1][capacity-weight[i-1]],
                                         board[i-1][capacity]
                                     );
                /**
                int taken_profit = profit[i-1]+board[i-1][capacity-weight[i-1]];
                int not_taken_profit = board[i-1][capacity];

                if(taken_profit > not_taken_profit)
                    marker[i][capacity] = 1;
                else
                    marker[i][capacity] = 0;
                */
            }
        }
    }

    int ans = board[items][sack_size];

    /**
    /// This is just to view the calculations

    for(int i=0; i<=items; i++)
    {
        if(!i)
            continue;
        for(int capacity=0; capacity<=sack_size; capacity++)
        {
            if(!capacity)
                continue;
            cout<<marker[i][capacity]<<"("<<board[i][capacity]<<")  ";
        }
        cout<<endl;
    }
    */

    /**
    /// print the item list that've been taken

    while(items)
    {
        if(!marker[items][sack_size])
            items--;
        else
        {
            cout<<"Item no.: "<<items-1<<", Weight: "<<weight[items-1]<<", Profit: "<<profit[items-1]<<endl;
            sack_size -= weight[items-1];
            items--;
        }
    }
    */

    return ans;
}


int main()
{
    /// Make the commented code `ACTIVE` to print the list

    int items = 4;
    int weight[] = {1, 3, 4, 5};
    int profit[] = {1, 4, 5, 7};
    int bag_size = 7;

    int ans = binary_knapsack(weight, profit, items, bag_size);
    cout<<ans<<endl;


    return 0;
}
