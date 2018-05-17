#################################################  
# kmeans: k-means cluster  
# Author : zouxy  
# Date   : 2013-12-25  
# HomePage : http://blog.csdn.net/zouxy09  
# Email  : zouxy09@qq.com  
#################################################  
  
from numpy import *  
import time  
import matplotlib.pyplot as plt  
  
  
# 计算欧式距离
def euclDistance(vector1, vector2):  
    return sqrt(sum(power(vector2 - vector1, 2)))  
  
# 初始化质心随机样本
def initCentroids(dataSet, k):  
    numSamples, dim = dataSet.shape  
    centroids = zeros((k, dim))  
    for i in range(k):  
        index = int(random.uniform(0, numSamples))  
        centroids[i, :] = dataSet[index, :]  
    return centroids  

# k-means cluster  
def kmeans(dataSet, k):  
    numSamples = dataSet.shape[0]  
    # first column stores which cluster this sample belongs to,  
    # second column stores the error between this sample and its centroid  
    clusterAssment = mat(zeros((numSamples, 2)))  
    clusterChanged = True  
  
    ## step 1:初始化聚类中心  
    centroids = initCentroids(dataSet, k)  
    #循环遍历数据
    while clusterChanged:  
        clusterChanged = False  
        ## for each sample  
        for i in range(numSamples):  
            minDist  = 100000.0  
            minIndex = 0  
            ## for each centroid  
            ## step 2: 计算距离中心点的距离   
            for j in range(k):  
                distance = euclDistance(centroids[j, :], dataSet[i, :])  
                if distance < minDist:  
                    minDist  = distance  
                    minIndex = j  
              
            ## step 3:更新聚类分配  
            if clusterAssment[i, 0] != minIndex:  
                clusterChanged = True  
                clusterAssment[i, :] = minIndex, minDist**2  
  
        ## step 4:更新聚类中心  
        for j in range(k):  
            pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]  
            centroids[j, :] = mean(pointsInCluster, axis = 0)  
  
    print ('Congratulations, cluster using k-means complete!')  
    return centroids, clusterAssment  


# bisecting k-means cluster  
def biKmeans(dataSet, k):  
    numSamples = dataSet.shape[0]  
    # first column stores which cluster this sample belongs to,  
    # second column stores the error between this sample and its centroid  
    clusterAssment = mat(zeros((numSamples, 2)))  
  
    # step 1: the init cluster is the whole data set  
    centroid = mean(dataSet, axis = 0).tolist()[0]  
    centList = [centroid]  
    for i in range(numSamples):  
        clusterAssment[i, 1] = euclDistance(mat(centroid), dataSet[i, :])**2  
  
    while len(centList) < k:  
        # min sum of square error  
        minSSE = 100000.0  
        numCurrCluster = len(centList)  #当前的簇的个数
        # for each cluster  
        #找出numCurrCluster簇中哪个簇分解得到的误差平方和最少的簇
        for i in range(numCurrCluster):  
            # step 2: get samples in cluster i  
            #选取第i个簇的所有数据，然后将其分成两个簇
            pointsInCurrCluster = dataSet[nonzero(clusterAssment[:, 0].A == i)[0], :]  
  
            # step 3: cluster it to 2 sub-clusters using k-means  
            #centroids的元素为每个簇的质心
            #splitClusterAssment第一列为样本所属的类别号，第二列为样本到其所属簇的质心的距离的平方
            centroids, splitClusterAssment = kmeans(pointsInCurrCluster, 2)  
  
            # step 4: calculate the sum of square error after split this cluster 求误差平方和
            splitSSE = sum(splitClusterAssment[:, 1])  
            notSplitSSE = sum(clusterAssment[nonzero(clusterAssment[:, 0].A != i)[0], 1])  
            currSplitSSE = splitSSE + notSplitSSE    #当前所有簇的平方和
  
            # step 5: find the best split cluster which has the min sum of square error  
            if currSplitSSE < minSSE:  
                minSSE = currSplitSSE  
                bestCentroidToSplit = i  
                bestNewCentroids = centroids.copy()  
                bestClusterAssment = splitClusterAssment.copy()  
  
        # step 6: modify the cluster index for adding new cluster  
         #将新分出来的两个簇的标号一个沿用它父亲的标号，一个用簇的总数来标号
        bestClusterAssment[nonzero(bestClusterAssment[:, 0].A == 1)[0], 0] = numCurrCluster  
        bestClusterAssment[nonzero(bestClusterAssment[:, 0].A == 0)[0], 0] = bestCentroidToSplit  
  
        # step 7: update and append the centroids of the new 2 sub-cluster  
        centList[bestCentroidToSplit] = bestNewCentroids[0, :]  #将第一个子簇的质心放在父亲质心的原位置
        centList.append(bestNewCentroids[1, :])  #将第二个子簇的质心添加在末尾
  
        # step 8: update the index and error of the samples whose cluster have been changed  
        #由第i个簇分解为j、k两个簇所得到的数据将分解之前的数据替换掉
        clusterAssment[nonzero(clusterAssment[:, 0].A == bestCentroidToSplit), :] = bestClusterAssment  
  
    print ('Congratulations, cluster using bi-kmeans complete!')  
    return mat(centList), clusterAssment  
  
# show your cluster only available with 2-D data  
def showCluster(dataSet, k, centroids, clusterAssment):  
    numSamples, dim = dataSet.shape  
    if dim != 2:  
        print ("Sorry! I can not draw because the dimension of your data is not 2!")  
        return 1  
  
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']  
    if k > len(mark):  
        print ("Sorry! Your k is too large! please contact Zouxy")  
        return 1  
  
    # draw all samples  
    for i in range(numSamples):  
        markIndex = int(clusterAssment[i, 0])  
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])  
  
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']  
    # draw the centroids  
    for i in range(k):  
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)  
          
    plt.show()  


'''将所有数据点看成一个簇 
当簇数目小于k时 
            对每一个簇 
                    计算总误差 
                    在给定的簇上面进行k-均值聚类（k=2） 
                    计算将该簇一分为二后的总误差 
            选择使得误差最小的那个簇进行划分操作
'''

'''

由于传统的KMeans算法的聚类结果易受到初始聚类中心点选择的影响，因此在传统的KMeans算法的基础上进行算法改进.
对初始中心点选取比较严格，各中心点的距离较远，这就避免了初始聚类中心会选到一个类上，一定程度上克服了算法陷入局部最优状态。
二分KMeans(Bisecting KMeans)算法的主要思想是：首先将所有点作为一个簇，然后将该簇一分为二。之后选择能最大限度降低聚类代价函数（也就是误差平方和）的簇划分为两个簇。
以此进行下去，直到簇的数目等于用户给定的数目k为止。以上隐含的一个原则就是：因为聚类的误差平方和能够衡量聚类性能，该值越小表示数据点越接近于他们的质心，聚类效果就越好。
所以我们就需要对误差平方和最大的簇进行再一次划分，因为误差平方和越大，表示该簇聚类效果越不好，越有可能是多个簇被当成了一个簇，所以我们首先需要对这个簇进行划分。
'''