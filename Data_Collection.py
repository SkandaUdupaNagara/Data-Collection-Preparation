import json
import pandas as pd
import urllib.request

link = 'http://api.worldbank.org/'  #url link of the web api
timeline = "1970:2018"  #Data collected between these period
#key features selected are GDP,Unemployment, Population and military expenses
query_indicators = ['NY.GDP.MKTP.CD','SL.UEM.TOTL.ZS','SP.POP.TOTL','MS.MIL.XPND.GD.ZS']

#function to get data for a given country 
def get_data(cIndicator):
    data=[]
    for qindi in query_indicators:    # loop for all querry indicaters
        url=link+'countries/'+cIndicator+'/indicators/'+qindi+'?per_page=100&date='+timeline+'&format=json' # form the url for a feature
        response=urllib.request.urlopen(url)  #request the data through url
        jsonData = response.read().decode('utf-8')  # read the data in the utf-8 format
        data1=json.loads(jsonData)   # load json object and form a python data structure
        data.append(data1)       # collect data for selected the features
        response.close()
    return data

#function to write data for a country with features
header=""
def writeData(cIndicator):    
    toWritecsv= open(cIndicator+".csv",'w')  #open file in write mode
    headers=[]   # creating header for columns
    headers.append('Year,')
    headers.append('GDP in USD,') #GDP of a country
    headers.append('Unemployment(%),') #Unemployment
    headers.append('Population,') #Total population
    headers.append('Military expenditure(% of GDP)') #Military expenditures
    headers.append('\n')

    header="".join(headers)   
    toWritecsv.write(header)
    year=0
    data=get_data(cIndicator)    
    for data2 in data[0][1]:
        toWritecsv.write(data2['date'])          # write year column
        toWritecsv.write(","+ifNaN(data2['value']))  
        # selecting 4 features
        for query in range(1,4):
            toWritecsv.write(","+ifNaN(data[query][1][year]['value']))
        toWritecsv.write('\n')
        year=year+1 
    toWritecsv.close()

def ifNaN(arg):  # check if NaN is present then return empty string
    if(arg is None):
        return ''
    else:
        return arg
    
writeData('IN')   # write file for India country
writeData('US')   # write file for USA country
writeData('CN')   # write file for China country
writeData('IE')   # write file for Ireland country
