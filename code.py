import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import statistics
import random
import pandas as pd

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].to_list()

#fig=ff.create_distplot([score],["score"],show_hist=False)
#fig.show()

mean=statistics.mean(data)
sd=statistics.stdev(data)
print("mean:",mean)
print("sd:",sd)
#sd is very high. this shows that distribution is very high
#the figure does not show a bell curve.Therefore we can take 100 random samples and find mean and sd 1000 times-sampling distribution.

#sampling distribution
def random_set_of_mean(counter):
    data_set=[]
    for i in range (0,counter):
        random_number=random.randint(0,len(data)-1)
        value=data[random_number]
        data_set.append(value)
    mean_sample=statistics.mean(data_set)
    return mean_sample

mean_list=[]
for i in range (0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)

#calculating mean and sd of sampling distribution
sd_sampl_dist=statistics.stdev(mean_list)
mean_sampl_dist=statistics.mean(mean_list)
print("mean of sampling distribution:",mean_sampl_dist)
print("sd of sampling distribution:",sd_sampl_dist)

fig=ff.create_distplot([mean_list],["mean_list"],show_hist=False)
fig.show()
