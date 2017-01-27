from numpy import vstack
from scipy.cluster.vq import kmeans, vq
import pygal

AgevsClass=[]
AgeVsFare_Data= []
PClassVsFare_Data = []
with open('titanic.csv','r') as Input:
    Input.readline() #Skip the header
    Data = Input.readline()  # Read 2nd line from CSV
    for line in Input:
        Data = line.split(',') # Create a list of the data
        PClass = float(Data[0])
        Age = float(Data[2])
        Fare = float(Data[3].rstrip('\r\n'))
        AgevsClass.append((Age,PClass))
        AgeVsFare_Data.append((Age, Fare))
        PClassVsFare_Data.append((PClass, Fare))

ClusterData = vstack(AgeVsFare_Data)
ClusterNumber = input("Enter the number of clusters : ")
# computing K-Means with K = 2 (2 clusters)
centroids, _ = kmeans(ClusterData, ClusterNumber)
# assign each sample to a cluster
xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'Clustering'
xy_chart.x_title = 'Age'
xy_chart.y_title = 'Fare'
idx, _ = vq(ClusterData, centroids)     # Change input according to graph plot
for num in range(0,ClusterNumber):
    xDataSize = ClusterData[idx==num,0].size
    yDataSize = ClusterData[idx==num,1].size
    xDataArray = list()
    yDataArray = list()
    xyDataElements = []
    for i in ClusterData[idx==num,0]:
        xDataArray.append(i)
    for i in ClusterData[idx==num,1]:
        yDataArray.append(i)
    #print yDataArray
    for i in range(0,xDataSize):
        xyDataElements.append((float(xDataArray[i]),float(yDataArray[i])))
    print xyDataElements
    s = "cluster"+ str(num)
    xy_chart.add(s, xyDataElements)
xClusterArray = list()
yClusterArray = list()
xyCusterElements = []
x =  centroids[:,0].size
for i in centroids[:,0]:
    xClusterArray.append(i)
for i in centroids[:,1]:
    yClusterArray.append(i)
for i in range(0,x):
    xyCusterElements.append((float(xClusterArray[i]),float(yClusterArray[i])))
xy_chart.add('Centroid', xyCusterElements)
xy_chart.render_to_file('ScatterPlot.svg')                          # Save the svg to a file