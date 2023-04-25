class Solution{
    public:
    bool is_possible_to_get_seats(int n, int m, vector<int>& seats){
        if(n==1&&m==1&&seats[0]==0)
        return 1;
        int i=0;
        if(seats[i]==0&&i+1<m&&seats[i+1]!=1){
        seats[i]=1;
        n--;
        }
        i++;
        while(n&&i<m){
            if(seats[i]==0){
                if(i-1>=0&&seats[i-1]!=1&&i+1<m&&seats[i+1]!=1){
                    seats[i]=1;
                    n--;
                }
                else if(i-1>=0&&seats[i-1]!=1&&i+1>=m){
                    seats[i]=1;
                    n--;
                }
            }
            i++;
        }//satwik
        if(n==0)
        return 1;
        return 0;
    }
};
