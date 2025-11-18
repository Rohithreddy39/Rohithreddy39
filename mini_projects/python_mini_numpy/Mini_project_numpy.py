#Mini-Project
#Project A: Weather Temperature Analysis
import numpy as np

#Step-1 Creating Dataset..
np.random.seed(42) #Reproducible results

# Generating temperatures between 15*c and 40*c .
temps=np.random.randint(15,40,size=(7,24))
print(temps)
print("Shape: ",temps.shape)

print("----------------------------------------")


#Step-2 Extract Specific Temperatures(Indexing & slicing)
#2.1 Temp on Day 3 at 5PM.
print(temps[2,17])
#2.2 All temps for Day 1
print(temps[0])
#2.3 All temps at 8AM for entire week.
print(temps[:,8])
#2.4- Temps for Days 2 to 4(rows 1 to 3)
print(temps[1:4])
#2.5 Temps for hours 6 to 10 for Day 5
print(temps[4,6:11])

print("----------------------------------------")


#Step-3 Daily Statistics(Mean, Max, Min, Range)
#3.1 Avg temp for each day
daily_avg=np.mean(temps,axis=1)
print("Daily Average Tempeartures:\n",daily_avg)

#3.2 Maximum Temp for each day
daily_max=np.max(temps,axis=1)
print("Daily maximum temperatures:\n",daily_max)
#3.3 Minimum temp for each day
daily_min=np.min(temps,axis=1)
print("Daily minimum temperatures:\n",daily_min)
#3.4 Daily Temp range
daily_range=daily_max-daily_min
print("Daily Temperature Range:\n",daily_range)

print("----------------------------------------")



#Step-4 Hourly statistics (Peak Hour, Coolest Hour, Patterns)
#4.1 Average Temperatures for each hour(Accross all 7 days)
hourly_avg=np.mean(temps,axis=0)
print("Hourly Average Temperatures:\n", hourly_avg)

#4.2 Hottest hour of the day
hottest_hour=np.argmax(hourly_avg)
print("Hottest hour Index: ",hottest_hour)

#4.3 Coolest hour of the day
coldest_hour=np.argmin(hourly_avg)
print("Coldest Hour Index:", coldest_hour)

#4.4 Max temps per hour
hourly_max=np.max(temps,axis=0)
print("Hourly max temp:\n",hourly_max)


print("----------------------------------------")


#Step-5 Extreme Temperatures(Above 35*c)
#5.1 Find all temps above 35*c
extreme_temps=temps[temps>35]
print("Extreme Temps (>35°C):\n", extreme_temps)

#5.2 Count of Extreme Temperatures
count_extreme=np.sum(temps>35)
print("Total Extreme Values:", count_extreme)

#5.3 Percentage of Extreme Readings
percent_extreme = (count_extreme / temps.size) * 100
print("Percentage of Extreme Temps:", percent_extreme)

print("----------------------------------------")

#Step-6 Flattening & Normalizing the Dataset(ML-ready data)
#6.1 Flatten the dataset(convert 7x24 to 1D array of 168 values)
flat=temps.ravel()
print("Flattened:\n",flat)
print("Shape:",flat.shape)

#6.2 Normalize the temperatures(min-max scaling)
#Formula - normalized_value = (x - min) / (max - min)
norm=(temps-temps.min())/(temps.max()-temps.min())
print("Normalized Temperatures:\n",norm)


print("----Project successfully Completed----")


