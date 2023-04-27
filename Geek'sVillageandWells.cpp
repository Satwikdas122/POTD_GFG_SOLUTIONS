class Solution{
public:
    vector<vector<int>> chefAndWells(int n,int m,vector<vector<char>> &arr){
        vector<vector<int>> ans(n,vector<int>(m,-1));
        queue<pair<pair<int,int>,int>> q;

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(arr[i][j] == 'N' || arr[i][j] == 'W'){
                    ans[i][j] = 0;
                }
                if(arr[i][j] == 'W'){
                    q.push({{i,j},0});
                }
            }
        }

        vector<pair<int,int>> dir = {{0,-1},{0,1},{-1,0},{1,0}};

        while(q.size() != 0){
            pair<pair<int,int>,int> front = q.front();
            q.pop();

            int i = front.first.first;
            int j = front.first.second;
            int currSteps = front.second;

            for(auto it:dir){
                int newI = i + it.first;
                int newJ = j + it.second;

                if(newI < 0 || newI >= n || newJ < 0 || newJ >= m || ans[newI][newJ] != -1){
                    continue;
                }

                if(arr[newI][newJ] == 'W' || arr[newI][newJ] == 'N'){
                    continue;
                }

                q.push({{newI,newJ},currSteps+1});
                ans[newI][newJ] = currSteps+1;
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(ans[i][j] != -1){
                    ans[i][j] *= 2;
                }
                if(arr[i][j] == '.'){
                    ans[i][j] = 0;
                }
            }
        }

        return ans;
    }
};
