/*
    **  if str1[i] == str2[j]:
          dp[i][j] = pd[i-1][j-1]
        else:
            dp[i][j] = min(pd[i-1][j], pd[i][j-1], pd[i-1][j-1]) + 1
*/


#include<bits/stdc++.h>
using namespace std;


int main()
{
    ios_base::sync_with_stdio(false);
    // freopen("in.txt", "r", stdin);

    string str1, str2;

    cin>>str1>>str2;
    /// '-' has been added to keep the match with the `DP` array
    str1 = '-' + str1;
    str2 = '-' + str2;

    int len1 = str1.length();
    int len2 = str2.length();

    int dp[len1][len2];
    char source[len1][len2];

    /// #Operations needed to convert str1 to `an empty string`
    for(int i=0; i<len1; i++)
        dp[i][0] = i;
    /// #Operations needed to convert `an empty string` to str2
    for(int i=0; i<len2; i++)
        dp[0][i] = i;

    for(int i=1; i<len1; i++)
    {
        for(int j=1; j<len2; j++)
        {
            if(str1[i] == str2[j])
            {
                dp[i][j] = dp[i-1][j-1];

                /// keep track of the change made
                source[i][j] = 'd';
            }
            else
            {
                int min_val = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]);
                dp[i][j] = min_val + 1;

                /// keep track of the change made
                if(min_val == dp[i-1][j-1])
                    source[i][j] = 'd'; /// d -> upper-left diagonal
                else if(min_val == dp[i-1][j])
                    source[i][j] = 't'; /// t -> top
                else
                    source[i][j] = 'l'; /// l -> left
            }
        }
    }

    cout<<"Minimum Edit Distance: "<<dp[len1-1][len2-1]<<endl;

    /*
    /// Printing the dp[][] array
    cout<<"\nCalculation"<<endl;
    for(int i=1; i<len1; i++)
    {
        for(int j=1; j<len2; j++)
            cout<<dp[i][j]<<source[i][j]<<" ";
        cout<<endl;
    }
    cout<<endl;
    */



    /// Now, using source[][], we'll find the operations


    cout<<"\nOperations:\n--------------"<<endl;

    int pos1 = len1-1, pos2 = len2-1, a=0;

    while(pos1 and pos2)
    {
        if(source[pos1][pos2] == 'd')
        {
            if(dp[pos1][pos2] > dp[pos1-1][pos2-1]) /// d: Change char, when `min` comes from left-top Diagonal
                cout<<"Change character \""<<str1[pos1]<<"\" at "<<pos1<<" into "<<str2[pos2]<<endl;
            else if(pos2 == 1)
            {
                for(int i=pos1-1; i>0; i--)
                    cout<<"Delete character \""<<str1[i]<<"\" at "<<i<<endl;
            }
            else if(pos1 == 1)
            {
                for(int i=pos2-1; i>0; i--)
                    cout<<"Add character \""<<str2[i]<<"\" before position 1"<<endl;
            }
            pos1--;
            pos2--;
        }
        else if(source[pos1][pos2] == 't') /// t: Delete char, when `min` comes from Top
        {
            cout<<"Delete character \""<<str1[pos1]<<"\" at "<<pos1<<endl;
            pos1--;
        }
        else /// l: Add char, when `min` comes from Left
        {
            cout<<"Add character \""<<str2[pos2]<<"\" after position "<<pos1<<endl;
            pos2--;
        }
    }


    return 0;
}

