
class Solution{
public:
    int dominantPairs(int n,vector<int> &arr){
        int counter = 0;
        int k =n/2;
        sort(arr.begin(),arr.begin()+k);
        sort(arr.begin()+k,arr.end());

        int i =0,j=n/2;
        while(i<k && j<n){
            if(arr[i]>=arr[j]*5){
                counter+=k-i;
                j++;

            }
            else{
                i++;
            }
        }
        return counter;
    }  
};
