def maxi(arr):
    max=arr[0]
    min=arr[0]
    size=len(arr)
    low=len(arr)
    for i in range(size):
        if(arr[i]>max):
            max=arr[i]
           # print(arr[i])
    for j in range(low):
        if(arr[j]<min):
            min=arr[j]
    #print(arr[j])
    sum=max-min
    print(sum)
            
arr=[61,45,95,36,84,43,25]
maxi(arr)
