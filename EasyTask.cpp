class Solution{
public:
    vector<char> easyTask(int n,string s,int q,vector<vector<string>> &queries){
        vector<char> v;

      for(int i=0;i<q;i++) {

          if(queries[i][0]=="1") {
              int index=stoi(queries[i][1]);
               s[index]=queries[i][2][0];
          }
          else {

              int start=stoi(queries[i][1]);
              int end=stoi(queries[i][2]);
              int k=stoi(queries[i][3]);

             int freq[26]={0};
                 int count=0 ;

             for(int j=start;j<=end;j++ ) {
                 freq[s[j]-'a']++;
             }

             for(int j=25;j>=0;j--) {
                 count+=freq[j];
                 if(count>=k)
                 {
                     count=j+'a';
                     break;
                 }
             }

              v.push_back(count);

          }
      }

      return v;
    }
};
