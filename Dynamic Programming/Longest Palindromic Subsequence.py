/*
    ** Make all substring of length 1 as palindrome
        for i = 0 to string_length-1
            board[i][i] = 1;
    ** Now, use the following conditions to evaluate for all the substrings of length > 1
        if string[i] == string[i+substring_length-1]:
            board[i][i+substring_length-1] = 2 + board[i+1][i+substring_length-2]
        else:
            board[i][i+substring_length-1] = max(board[i+1][i+substring_length-1], board[i][i+substring_length-2])
*/


#include<bits/stdc++.h>
using namespace std;

typedef long long ll;


int main()
{
    ios_base::sync_with_stdio(false);
    // freopen("in.txt", "r", stdin);

    /// sample input: annqwnbvexrvttyafgatrqqewghiqlp
    /// sample output: length-> 13, palindromic subsequence: qwertafatrewq
    string str;

    cin>>str;

    int len;
    len = str.length();

    int board[len][len];
    pair<int, int> source[len][len];

    for(int i=0; i<len; i++)
        board[i][i] = 1;

    for(int t=2; t<=len; t++)
    {
        for(int i=0; (i+t-1)<len; i++)
        {
            if(str[i] == str[i+t-1])
            {
                board[i][i+t-1] = 2;
                if(t>2)
                {
                    board[i][i+t-1] += board[i+1][i+t-2];

                    /// source array keeps track of the chars of the subsequence
                    source[i][i+t-1] = {i+1, i+t-2};
                }
            }
            else
            {
                board[i][i+t-1] = max(board[i+1][i+t-1], board[i][i+t-2]);

                /// source array keeps track of the chars of the subsequence
                if(board[i+1][i+t-1] >= board[i][i+t-2])
                    source[i][i+t-1] = {i+1, i+t-1};
                else
                    source[i][i+t-1] = {i, i+t-2};

            }
        }
    }

    cout<<"Longest palindromic subsequence length: "<<board[0][len-1]<<endl;


    /// Using the source[][], it is easy to get the `Longest Palindromic Subsequence`

    int posx = 0, posy = len-1;
    int srcx = source[posx][posy].first;
    int srcy = source[posx][posy].second;

    string ans = "";

    while(posx < posy)
    {
        if((posx+1) == srcx and (posy-1) == srcy)
            ans = str[posx] + ans;

        posx = srcx;
        posy = srcy;

        srcx = source[posx][posy].first;
        srcy = source[posx][posy].second;

        int dif = posy - posx;
        if(dif < 2)
        {
            string original = ans;
            reverse(ans.begin(), ans.end());
            if(dif and str[posx] == str[posy])
            {
                ans = ans + str[posx] + str[posy] + original;
            }
            else
                ans = ans + str[posx] + original;

            break;
        }
    }
    cout<<"Longest palindromic subsequence: "<<ans<<endl;


    return 0;
}

