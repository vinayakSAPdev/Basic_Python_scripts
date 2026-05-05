# import pandas as pd

# #load my csv file
# data = pd.read_csv('datasets/weather_report.csv')


# # print(data.head())

# # print(data['Temperature'])
# # print(data['Temperature'][9])
# # print(data[['Temperature', 'Humidity']])
# # print(data[data['Temperature'] > 30])
# # print(data[(data['Temperature'] > 30) & (data['Temperature'] < 70)])
 
# #  #get the data on which the weather is rain
# # print(data[['Sunrise', 'Sunset']][data['Event'] == 'Rain'])

# # #adding new column and fill it with the value of temperature in fahrenheit
# # data['Temperature_F'] = data['Temperature'] * 9/5 + 32
# # print(data)

# # mean wind speed
# # mean_wind_speed = data['Wind Speed'].mean()
# # print("Mean Wind Speed:", mean_wind_speed)

# # #inplace change the value of the column event to sunny if the value is clear
# # print(data)
# # data['Event'].replace('Clear', 'Sunny', inplace=True)
# # print(data)
# #fillna value in the column event with the value of sunny if the value is clear
# data['Event'].fillna('Sunny', inplace=True) 
# print(data)
# j

