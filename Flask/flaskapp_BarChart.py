from flask import Flask, render_template, request, redirect
from flask import flash, request, session, abort, url_for
import pygal
from numpy import vstack
from scipy.cluster.vq import kmeans, vq

app = Flask(__name__)


@app.route("/")
def IndexPage():
    return render_template('index.html')

@app.route("/select",methods=['GET', 'POST'])
def Show_Graph():
    if request.method == "POST":
        #with open('/home/ubuntu/flaskapp/titanic.csv', 'r') as Input:
        with open('UNPrecip.csv', 'r') as Input:
            Country = []
            monthmax=[]
            Jan1 =[]
            Feb1 =[]
            Mar1 =[]
            April1 =[]
            May1 =[]
            June1 =[]
            July1 =[]
            Aug1 =[]
            Sep1 =[]
            Oct1 =[]
            Nov1 =[]
            Dec1 =[]
            Input.readline()  # Skip the header
        #     Data = Input.readline()  # Read 2nd line from CSV
            for line in Input:
                Data = line.split(',')  # Create a list of the data
                Jan = float(Data[0])
                Feb = float(Data[1])
                Mar = float(Data[2])
                April = float(Data[3])
                May = float(Data[4])
                June = float(Data[5])
                July = float(Data[6])
                Aug = float(Data[7])
                Sep = float(Data[8])
                Oct = float(Data[9])
                Nov = float(Data[10])
                Dec = float(Data[11].rstrip('\r\n'))
                # Append data to array
                Jan1.append(Jan)
                Feb1.append(Feb)
                Mar1.append(Mar)
                April1.append(April)
                May1.append(May)
                June1.append(June)
                July1.append(July)
                Aug1.append(Aug)
                Sep1.append(Sep)
                Oct1.append(Oct)
                Nov1.append(Nov)
                Dec1.append(Dec)
                monthmax.append("1",max(Jan1))
                monthmax.append("1",max(Jan1))
                monthmax.append("1",max(Jan1))
                monthmax.append("1",max(Jan1))
                monthmax.append("1",max(Jan1))
                monthmax.append("1",max(Jan1))
                monthmax.append("1",max(Jan1))
                monthmax.append("1",max(Jan1))
                monthmax.append("1",max(Jan1))
        ClusterData = vstack(monthmax)  # Change input according to graph plot
        input1 = request.form["ClusterNumber"]
        ClusterNumber = int(input1)
        # computing K-Means with K = 2 (2 clusters)
        centroids, _ = kmeans(ClusterData, ClusterNumber)
        # assign each sample to a cluster
        # xy_chart = pygal.XY(stroke=False)
        # xy_chart.title = 'Clustering'
        # xy_chart.x_title = 'Survived'
        # xy_chart.y_title = 'Fare'
        # idx, _ = vq(ClusterData, centroids)
        # for num in range(0, ClusterNumber):
        #     xDataSize = ClusterData[idx == num, 0].size
        #     yDataSize = ClusterData[idx == num, 1].size
        #     xDataArray = list()
        #     yDataArray = list()
        #     xyDataElements = []
        #     for i in ClusterData[idx == num, 0]:
        #         xDataArray.append(i)
        #     for i in ClusterData[idx == num, 1]:
        #         yDataArray.append(i)
        #     for i in range(0, xDataSize):
        #         xyDataElements.append((float(xDataArray[i]), float(yDataArray[i])))
        #     s = "cluster" + str(num)
        #     xy_chart.add(s, xyDataElements)
        # xClusterArray = list()
        # yClusterArray = list()
        # xyCusterElements = []
        # x = centroids[:, 0].size
        # for i in centroids[:, 0]:
        #     xClusterArray.append(i)
        # for i in centroids[:, 1]:
        #     yClusterArray.append(i)
        # for i in range(0, x):
        #     xyCusterElements.append((float(xClusterArray[i]), float(yClusterArray[i])))
        # xy_chart.add('Centroid', xyCusterElements)
        # return xy_chart.render_response()

if __name__ == "__main__":
    app.run(debug=True)