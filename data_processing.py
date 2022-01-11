import pandas as pd
def filter_data(df,center,attr_name,tolerance=5):
    lat_name,lon_name,_ = attr_name
    return df[attr_name][(df[lat_name]>center[0]-tolerance) & (df[lat_name]<center[0]+tolerance) & (df[lon_name]>center[1]-tolerance) & (df[lon_name]<center[1]+tolerance)]
def convert_timestamp(df,time_name):
    df[time_name] =  pd.to_datetime(df[time_name])
    df[time_name] = df[time_name].values.astype('int64') // 10 ** 9
    return df

attr_name = ['lat','lon','t']

NewYork = pd.read_csv('New_York_Crashes_raw.csv')
center_NewYork = [40.730610,-73.935242]
attr_name_NewYork = ['LATITUDE','LONGITUDE','CRASH DATE']
NewYork.fillna(0,inplace=True)
NewYork = filter_data(NewYork,center_NewYork,attr_name_NewYork)
convert_timestamp(NewYork,attr_name_NewYork[2])
NewYork.columns = attr_name
NewYork.to_csv('NewYork.csv',index=False)

Seattle = pd.read_csv('Seattle_Crime_raw.csv')
center_Seattle = [47.608013,-122.335167]
attr_name_Seattle = ['Latitude','Longitude','Offense Start DateTime']
Seattle = filter_data(Seattle,center_Seattle,attr_name_Seattle)
convert_timestamp(Seattle,attr_name_Seattle[2])
Seattle.columns = attr_name
Seattle.to_csv('Seattle.csv',index=False)

Ontario = pd.read_csv('Ontario_org.csv')
center_Ontario = [43.000000,-81.000000]
attr_name_Ontario = ['Reporting_PHU_Latitude','Reporting_PHU_Longitude','Case_Reported_Date']
Ontario = filter_data(Ontario,center_Ontario,attr_name_Ontario)
convert_timestamp(Ontario,attr_name_Ontario[2])
Ontario.columns = attr_name
Ontario.to_csv('Ontario.csv',index=False)