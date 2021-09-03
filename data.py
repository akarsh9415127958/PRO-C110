import plotly.figure_factory as ff
import statistics 
import random
import plotly.graph_objects as go
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv") 
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("population mean:-",population_mean )
print("std_deviation:-",std_deviation)


# code to find the mean and standard deviation for 100 data times
dataset = []

for i in range(0,100):
     random_index= random.randint(0,len(data))
     value = data[random_index]
     dataset.append(value)
mean = statistics.mean(dataset)
std_deviation  =  statistics.stdev(dataset)
     
print("mean of sample:-",mean)

print("std-deviation of sample:-",std_deviation)


def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean




# Pass the number of time you want the mean of the data points as a parameter in range function in for loop
def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)
  
    
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

setup()


#Code to find the mean of the raw data ("population data")
population_mean = statistics.mean(data)
print("population mean:- ", population_mean)


# code to find the standard deviation of the sample data
def standard_deviation():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()