#include<bits/stdc++.h>
using namespace std;


/*
Input:
9 8
0 1
0 8
1 2
1 5
1 7
2 3
2 4
2 6
*/


vector<int> DFS(vector<int> graph[], int n, int source)
{
    vector<int> ans;
    stack<int> stk;
    bool is_visited[n];

    for(int i=0; i<n; i++)
        is_visited[i] = false;

    stk.push(source);
    is_visited[source] = true;

    while(!stk.empty())
    {
        int u = stk.top();
        stk.pop();
        ans.push_back(u);

        for(int i=0; i<graph[u].size(); i++)
        {
            int v = graph[u][i];
            if(!is_visited[v])
            {
                stk.push(v);
                is_visited[v] = true;
            }
        }
    }

    return ans;
}


int main()
{
    ios_base::sync_with_stdio(false);
//    freopen("in.txt", "r", stdin);

    int n, m;
    cin>>n>>m;

    vector<int> graph[n];

    int a, b;
    for(int i=0; i<m; i++)
    {
        cin>>a>>b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    vector<int> ans;
    int source = 0;
    ans = DFS(graph, n, source);

    for(int i=0; i<n; i++)
        cout<<ans[i]<<" "<<endl;


    return 0;
}

