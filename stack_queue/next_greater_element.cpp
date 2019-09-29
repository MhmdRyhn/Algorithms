#include<bits/stdc++.h>
using namespace std;


// This function actually returns the element's indices
vector<int> next_greater_element(int arr[], int n)
{
    stack<int> s; // Used to find previous and next smaller

    // Array to store next greater
    vector<int> next(n+1);
    for (int i = 0; i < n; i++)
        next[i] = n;

    // Find the next greater element's index for each element
    // NB: For PREVIOUS element's index, change the loop to -> for (int i = 0; i < n; i++)
    for (int i = n-1 ; i >= 0 ; i--)
    {
        // For SMALLER element revert the inequality to >= (greater than or equal to)
        while (!s.empty() && arr[s.top()] <= arr[i])
            s.pop();
        if(!s.empty())
            next[i] = s.top();

        s.push(i);
    }

    return next;
}


int main()
{
    int n=5;
    int a[] = {1, 9, 3, 7, 5};

    vector<int> ans;
    ans = next_greater_element(a, n);

    for (int i=0; i<n; i++)
        if(ans[i] >= n)
            cout<<"NULL ";
        else
            cout<< a[ans[i]] << " ";

    return 0;
}

