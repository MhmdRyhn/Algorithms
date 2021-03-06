// https://www.youtube.com/watch?v=ZmnqCZp9bBs


#include<bits/stdc++.h>

using namespace std;

#define ll long long


ll max_histogram_area(ll arr[], ll sz)
{
    stack<ll> stk;
    ll max_area = 0, area = 0;

    ll i = 0;
    while(i<sz)
    {
        if(stk.empty() or arr[i]>=arr[stk.top()])
        {
            stk.push(i);
            i++;
        }
        else
        {
            ll extracted_top = stk.top();
            stk.pop();

            if(stk.empty())
                area = arr[extracted_top] * i;
            else
                area = arr[extracted_top] * (i - stk.top() - 1);

            if(area > max_area)
                max_area = area;
        }
    }

    while(!stk.empty())
    {
        ll extracted_top = stk.top();
        stk.pop();

        if(stk.empty())
            area = arr[extracted_top] * i;
        else
            area = arr[extracted_top] * (i - stk.top() - 1);

        if(area > max_area)
            max_area = area;
    }

    return max_area;
}


int main()
{
    ios_base::sync_with_stdio(false);
//    freopen("in.txt", "r",stdin);

    ll arr[] = {2, 1, 2, 3, 1};

    ll ans = max_histogram_area(arr, 5);

    cout<< ans;

    return 0;
}

