class Solution 
{
    public:
   
    static bool cmp(Job& J1,Job& J2)
    {
        return J1.profit>J2.profit;
    }
        vector<int> JobScheduling(Job arr[], int n) 
        { 
           asis of Profit in descending order   
            sort(arr,arr+n,cmp);
            bool Deadline[100001]={0};
            int count=0,profit=0;
            for(int i=0;i<n;i++)
            {
                int currdead=arr[i].dead;
                int currprofit=arr[i].profit;
                while(currdead>=1 && Deadline[currdead]==1)
                {
                    currdead--;
                }
                if(currdead>=1)
                {
                    Deadline[currdead]=1;
                    profit+=currprofit;
                    count++;
                }
            }
            return {count,profit};
        }
};
