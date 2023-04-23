int m = arr[0];
        bool sp = true;
        for(int i = 1; i<n; i++) {
            if(m > arr[i]) m = arr[i];
            if(arr[i-1]%2 != arr[i]%2) sp = false;
        }
        return sp?m:1;
    }
};
