/*
    Say, strings are 1-indexed

    IF string1[i] == string2[j]:
        dp[i][j] = dp[i][j] + 1
    ELSE:
        dp[i][j] = 0

    Now, iterate through the `dp` array and pick the largest value
*/


#include<bits/stdc++.h>
using namespace std;

typedef long long ll;


int main()
{
    ios_base::sync_with_stdio(false);
    // freopen("in.txt", "r", stdin);

    string str1, str2;

    cin>>str1>>str2;

    int ls1, ls2;
    ls1 = str1.length();
    ls2 = str2.length();

    int board[ls1+1][ls2+1];

    for(int i=0; i<ls1+1; i++)
        board[0][i] = 0;
    for(int i=0; i<ls2+1; i++)
        board[i][0] = 0;

    int maxlen = 0, posx = -1, posy = -1;

    for(int i=1; i<ls1+1; i++)
    {
        for(int j=1; j<ls2+1; j++)
        {
            if(str1[i-1] == str2[j-1])
            {
                board[i][j] = board[i-1][j-1] + 1;
                if(board[i][j] > maxlen)
                {
                    maxlen = board[i][j];
                    posx = i - 1;
                    posy = j - 1;
                }
            }
            else
                board[i][j] = 0;
        }
    }
    cout<<"Lowest Common Substring Length: "<<maxlen<<endl;

    string maxstr = "";
    while(maxlen)
    {
        maxstr = str1[posx] + maxstr;
        posx--;
        maxlen -- ;
    }

    cout<<"Lowest Common Substring: "<<maxstr<<endl;


    return 0;
}

