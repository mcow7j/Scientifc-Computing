""" Your college id here:
    Template code for part 1, contains 4 functions:
    newSort, merge: codes for part 1.1
    time_newSort: to be completed for part 1.1
    findTrough: to be completed for part 1.2
"""
#import needed modules
import random
import time
import numpy as np
import matplotlib.pyplot as plt

def newSort(X,k=0):
    """Given an unsorted list of integers, X,
        sort list and return sorted list
    """

    n = len(X)
    if n==1:
        return X
    elif n<=k:
        for i in range(n-1):
            ind_min = i
            for j in range(i+1,n):
                if X[j]<X[ind_min]:
                    ind_min = j
            X[i],X[ind_min] = X[ind_min],X[i]
        return X
    else:
        L = newSort(X[:n//2],k)
        R = newSort(X[n//2:],k)
        return merge(L,R)


def merge(L,R):
    """Merge 2 sorted lists provided as input
    into a single sorted list
    """
    M = [] #Merged list, initially empty
    indL,indR = 0,0 #start indices
    nL,nR = len(L),len(R)

    #Add one element to M per iteration until an entire sublist
    #has been added
    for i in range(nL+nR):
        if L[indL]<R[indR]:
            M.append(L[indL])
            indL = indL + 1
            if indL>=nL:
                M.extend(R[indR:])
                break
        else:
            M.append(R[indR])
            indR = indR + 1
            if indR>=nR:
                M.extend(L[indL:])
                break
    return M


def time_newSort(N,k,Merge=False):
    """Analyze performance of newSort
    Use variables inputs and outputs if/as needed
    """
    import random
    import time

    #Generate random interger list
    randomlist = [random.randint(0, N) for iter in range(N)]
    #set up time list
    newsort_time=[]

    #records time of merge function
    if Merge:
        t1=time.time()
        list2=newSort(randomlist,0)
        t2=time.time()
        newsort_time.append(t2-t1)

    for i in range(0,len(k)):
        t1=time.time()
        list=newSort(randomlist,k[i])
        t2=time.time()
        newsort_time.append(t2-t1)


    return newsort_time


def findTrough(L):
    """Find and return a location of a trough in L
    """
    #find lenght of trough
    n = len(L)-1
    #check list is not empty
    if L==[]:
        return -n-2
    #check first and last elements
    if L[0]<=L[1]:
        return 0
    if L[n]<=L[n-1]:
        return n
    #set indexing
    ind=(n+1)//2
    #size of jump in indexing each step
    oldind=ind
    #for loop to limit how many numbers it checks and to work recursively
    for i in range(0,n):
      if L[ind]>L[ind-1]:
        oldind=oldind//2
        #max means it never gets stuck
        ind=ind-max(oldind,1)
      elif L[ind]<=L[ind+1]:
        return ind
      else:
        oldind=oldind//2
        #max stopts algoritm stop checking numbers
        ind=ind+max(oldind,1)
    return -n-2





if __name__=='__main__':
    #import needed modules
    import numpy as np
    import matplotlib.pyplot as plt

    Nlist=[10000,20000,30000,40000,50000]
    newsort_time=np.zeros((len(k)+1,len(Nlist)))
    for i in range(len(Nlist)):
        newsort_time[:,i]=time_newSort(Nlist[i],[9,Nlist[i]],Merge=True)
    #code generates first graph
    plt.figure(figsize=(12, 6))
    plt.plot(np.log2(Nlist)*Nlist,newsort_time[0,:],label="Merge sort")
    plt.plot(np.log2(Nlist)*Nlist,newsort_time[1,:],label="k=9")
    plt.plot(np.log2(Nlist)*Nlist,newsort_time[2,:],label="k=N")
    plt.xlabel(r' N $ \log_2(N) $',size=12)
    plt.ylabel('Computational time',size=12)
    plt.title('How large K effects Computational time',size=20)
    plt.legend(loc="center left",fontsize=12,fancybox=True, framealpha=1, shadow=True, borderpad=1)
    plt.show()

    #sets up test data for graph 2
    k=[2,9,20,50,80]
    Nlist=[1000,10000,100000,1000000]
    newsort_time=np.zeros((len(k)+1,len(Nlist)))
    for i in range(len(Nlist)):
        newsort_time[:,i]=time_newSort(Nlist[i],k,Merge=True)
    #code generates 2 graph
    plt.figure(figsize=(12, 6))
    plt.plot(np.log2(Nlist)*Nlist,newsort_time[0,:],label="Merge sort")
    plt.plot(np.log2(Nlist)*Nlist,newsort_time[1,:],label="k=2")
    plt.plot(np.log2(Nlist)*Nlist,newsort_time[2,:],label="k=9")
    plt.plot(np.log2(Nlist)*Nlist,newsort_time[3,:],label="k=20")
    plt.plot(np.log2(Nlist)*Nlist,newsort_time[4,:],label="k=50")
    plt.plot(np.log2(Nlist)*Nlist,newsort_time[5,:],label="k=80")
    plt.xlabel(r' N $ \log_2(N) $',size=12)
    plt.ylabel('Computational time',size=12)
    plt.title('How N effects Computational time taken for varying k',size=20)
    plt.legend(loc="center left",fontsize=12,fancybox=True, framealpha=1, shadow=True, borderpad=1)
    plt.show()

    #code for 3rd graoh gneterates data
    k=range(0,80)
    r=100
    newsort_time=np.zeros((len(k),1))
    for i in range(0,r):
      newsort_time[:,0]+=time_newSort(10000,k,Merge=False)
    newsort_time=newsort_time/r
    #code plots grpah
    plt.figure(figsize=(12, 6))
    plt.plot(k,newsort_time[:,0],label="K varying")
    plt.plot(k,newsort_time[0,0]*np.ones((len(k),1)),label="Merge sort")
    plt.xlabel('K',size=12)
    plt.ylabel('Computational time aver for 100 tests',size=12)
    plt.title('How K effects computational running time for N=10000 (optimum k)',size=20)
    plt.legend(loc="upper left",fontsize=12,fancybox=True, framealpha=1, shadow=True, borderpad=1)
    plt.show()

    #generates data for 3rd grpah
    k=range(0,80)
    r=10
    newsort_time=np.zeros((len(k),1))
    for i in range(0,r):
     newsort_time[:,0]+=time_newSort(100000,k,Merge=False)
    newsort_time=newsort_time/r
    #plots 4th graph
    plt.figure(figsize=(12, 6))
    plt.plot(k,newsort_time[:,0],label="K varying")
    plt.plot(k,newsort_time[0,0]*np.ones((len(k),1)),label="Merge sort")
    plt.xlabel('k',size=12)
    plt.ylabel('Computational time aver for 10 tests',size=12)
    plt.title('How K effects computational running time for N=100000 (optimum k)',size=20)
    plt.legend(loc="lower right",fontsize=12,fancybox=True, framealpha=1, shadow=True, borderpad=1)
    plt.show()


    return None
