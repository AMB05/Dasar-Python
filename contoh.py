#binary interpolationSearch
def Interpolation_Search (arr,target):
    start = 0
    end = len(arr)-1
    found = False

    while start <= end and found == False:
        if start == end:
            if arr[start] == target: 
                return "{} is at {} index".format(target,pos)
            return "not found"    

        pos = start + (((end-start)//(arr[end]-arr[start])) * (target-arr[start]))               

        if arr[pos] == target:      
            return "{} is at {} index".format(target,pos)  

        if arr[pos] < target:
            start = pos + 1;
        else:
            end = pos - 1;    

    return "Not Found"

arr = [10, 20, 40, 77, 86, 89, 91]
print(Interpolation_Search(arr, 86))