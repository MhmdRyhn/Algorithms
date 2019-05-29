/// Explanation: https://www.youtube.com/watch?v=WepWFGxiwRs&t=169s

#include<bits/stdc++.h>
using namespace std;

typedef struct details
{
    bool can_split;
    // `from` and `to` are to mark the split point
    int from, to;
} ss;


bool word_break(string s, map<string, bool> dict)
{
    int len = s.length();
    ss board[len][len];

    /*
    // Reset board

    for(int i=0; i<len; i++)
        for(int j=0; j<len; j++)
            board[i][j].can_split = false;
    */

    for(int l=1; l<=len; l++)
    {
        for(int i=0; (i+l-1)<len; i++)
        {
            int j = i + l - 1;
            string sub = s.substr(i, l);

            if(dict[sub])
                board[i][j].can_split = true;
            else
            {
                for(int k=i; k<j; k++)
                {
                    if(board[i][k].can_split and board[k+1][j].can_split)
                    {
                        board[i][j].can_split = true;
                        break;
                    }
                    else
                        board[i][j].can_split = false;
                }
            }
        }
    }

    /*
    // Print the board

    for(int i=0; i<len; i++)
    {
        for(int j=0; j<len; j++)
        {
            if(i>j)
                cout<<"*";
            else
                cout<<board[i][j].can_split;
            cout<<" ";
        }
        cout<<endl;
    }
    */

    return board[0][len-1].can_split;
}


int main()
{
    string s = "IAmAce";
    map<string, bool> dict;

    dict["I"] = true;
    dict["A"] = true;
    dict["Am"] = true;
    dict["Ace"] = true;

    cout<<word_break(s, dict)<<endl;

    return 0;
}

