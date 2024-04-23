# %%
import pandas as pd
import json

# %%
with open("./data/data.json","r") as f:
    data = (json.load(f))
for key,value in data.items():
	print(key, ':', value)
      
print(type(data))

# %%
times = data['list']
type(times)
for x in range(5):
    print(times[x])


# %%
time_array =[]
for item in times:
    time = item['dt_txt']
    time_array.append(time)
print(time_array)


wind_speed =[]
for item in times:
    time = item['wind']['speed']
    wind_speed.append(time)
print(wind_speed)

wind_deg =[]
for item in times:
    time = item['wind']['deg']
    wind_deg.append(time)
print(wind_deg)

wind_gust =[]
for item in times:
    time = item['wind']['gust']
    wind_gust.append(time)
print(wind_gust)

# %%
dict = {
    'datetime': time_array,
    'wind_speed': wind_speed,
    'wind_deg': wind_gust,
    'wind_gust': wind_gust
}

with open("./data/cleaned_data.json", "w") as json_file:
    json.dump(dict, json_file)

#df = pd.DataFrame(to_df)
#print(df)
#df.to_csv('data/cleaned_data.csv')


