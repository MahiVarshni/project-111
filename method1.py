import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import statistics
import random
import pandas as pd

#students who got tablet with learning material

df=pd.read_csv("sample.csv")
score=df["reading_time"].to_list()

#fig=ff.create_distplot([score],["score"],show_hist=False)
#fig.show()

mean=statistics.mean(score)
sd=statistics.stdev(score)
print("mean:",mean)
print("sd:",sd)

#before intervention, mean was 64 and after intervention mean increased to 65. 

z_score=(64.722-mean)/2.105
print("z-score:",z_score)
