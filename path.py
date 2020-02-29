import copy

def bst(arr,start,end,path,currnode):
    
    print(path,"path")
    print("current node",currnode)
    if(currnode==end-1):
        return path
    else:
        result=[]
        print(arr[currnode],"arr current node")
        for i in arr[currnode]:
            
            #visited.add(i)
            path_=copy.deepcopy(path)
            path_.append(i)
            print(path_,i,"path")
            
            temp=(bst(arr,start,end,path_,i)  )
            print(temp,"temp")
            if(len(temp)>=len(result)):
                result=copy.deepcopy(temp)
            path_=path    
        return result        

            
    


def main():
    num=16
    arr=[]
    for i in range(num):
        arr.append([])
    for i in range(num-1):
        temp=list(map(int,input().split(" ")))
        arr[temp[0]-1].append(temp[1]-1)
        
    start=0
    end=14
    print(arr)
    print(bst(arr,start,end,[start],start))
if __name__=="__main__":
    main()