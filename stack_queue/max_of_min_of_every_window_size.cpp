#include<bits/stdc++.h>
using namespace std;


vector<int> max_of_min(int arr[], int n)
{
    stack<int> s; // Used to find previous and next smaller

    // Arrays to store previous and next smaller
    int previous[n+1];
    int next[n+1];

    // Initialize elements of previous[] and next[]
    for (int i = 0; i < n; i++)
    {
        previous[i] = -1;
        next[i] = n;
    }

    // Find the previous smaller element's index
    for (int i = 0; i < n; i++)
    {
        while (!s.empty() && arr[s.top()] >= arr[i])
            s.pop();
        if (!s.empty())
            previous[i] = s.top();
        s.push(i);
    }

    // Empty the stack as stack is going to be used for next[]
    while (!s.empty())
        s.pop();

    // Find the next smaller element's index
    for (int i = n-1 ; i >= 0 ; i--)
    {
        while (!s.empty() && arr[s.top()] >= arr[i])
            s.pop();
        if(!s.empty())
            next[i] = s.top();
        s.push(i);
    }

    vector<int> ans(n+1);
    for(int i = 0; i <= n; i++)
        ans[i] = 0;

    for(int i = 0; i < n; i++)
    {
        int len = next[i] - previous[i] - 1;
        ans[len] = max(ans[len], arr[i]);
    }

    // Some entries in ans[] may not be filled yet. Fill
    // them by taking values from right side of ans[]
    for(int i = n-1; i >= 1; i--)
        ans[i] = max(ans[i], ans[i+1]);
    
    return ans;
}


int main()
{
    int n;
    cin >> n;
    int arr[n];

    for (int i = 0; i < n; i++) 
        cin>>arr[i];
    
    vector<int> ans = max_of_min(arr, n);

    for (int i=1; i<=n; i++)
        cout << ans[i] << " ";

    return 0;
}

