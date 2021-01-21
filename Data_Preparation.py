
import pandas as pd


# reading the data files as data frames
India_data = pd.read_csv('IN.csv')  
USA_data = pd.read_csv('US.csv')
China_data = pd.read_csv('CN.csv')
Ireland_data = pd.read_csv('IE.csv')


# Handling missing data. Replace missing values by the mean of the column
headers=['GDP in USD','Unemployment(%)','Population','Military expenditure(% of GDP)']
for column in headers:
    India_data[column]=India_data[column].fillna(India_data[column].mean())
    USA_data[column]=USA_data[column].fillna(USA_data[column].mean())
    China_data[column]=China_data[column].fillna(China_data[column].mean())
    Ireland_data[column]=Ireland_data[column].fillna(Ireland_data[column].mean())

dataUSA=USA_data.drop('Year',1)  #removing year column from summary statistics
dataUSA.describe()  #summaries the data for country USA
dataIndia=India_data.drop('Year',1)  #removing year column from summary statistics
dataIndia.describe()  #summaries the data for country India
dataChina=China_data.drop('Year',1)  #removing year column from summary statistics
dataChina.describe()  #summaries the data for country China
dataIreland=Ireland_data.drop('Year',1)  #removing year column from summary statistics
dataIreland.describe()  #summaries the data for country Ireland

plt.title("Yearly Military expenditure and GDP in USA since July 1970\n")
plt.stackplot(USA_data.iloc[:,0],[USA_data.iloc[:,4], USA_data.iloc[:,2]], 
          colors=['#4771A6','#85BA89'])

plt.legend([mpatches.Patch(color='#4771A6'),  
            mpatches.Patch(color='#85BA89'),], 
           ['Military expenditure (% of GDP)','GDP'])
plt.show()

plt.title("Yearly Military expenditure and GDP in India since July 1970\n")
plt.stackplot(India_data.iloc[:,0],[India_data.iloc[:,4], India_data.iloc[:,2]], 
          colors=['#4771A6','#85BA89'])

plt.legend([mpatches.Patch(color='#4771A6'),  
            mpatches.Patch(color='#85BA89'),], 
           ['Military expenditure (% of GDP)','GDP'])
plt.show()

plt.title("Yearly Military expenditure and GDP in India since July 1970\n")
plt.stackplot(India_data.iloc[:,0],[India_data.iloc[:,4], India_data.iloc[:,2]], 
          colors=['#4771A6','#85BA89'])

plt.legend([mpatches.Patch(color='#4771A6'),  
            mpatches.Patch(color='#85BA89'),], 
           ['Military expenditure (% of GDP)','GDP'])
plt.show()

plt.title("Yearly Military expenditure and GDP in Ireland since July 1970\n")
plt.stackplot(Ireland_data.iloc[:,0],[Ireland_data.iloc[:,4], Ireland_data.iloc[:,2]], 
          colors=['#4771A6','#85BA89'])

plt.legend([mpatches.Patch(color='#4771A6'),  
            mpatches.Patch(color='#85BA89'),], 
           ['Military expenditure (% of GDP)','GDP'])
plt.show()

#plot the graph showing the variation of Unemployment rate for the various countries
plt.plot(India_data['Year'],India_data['Unemployment(%)'],'.-')
plt.plot(USA_data['Year'],USA_data['Unemployment(%)'],'.-')
plt.plot(China_data['Year'],China_data['Unemployment(%)'],'.-')
plt.plot(Ireland_data['Year'],Ireland_data['Unemployment(%)'],'.-')
plt.legend(['India', 'USA','China','Ireland'], loc='best')
plt.title("Unemployment aross 4 countries since 1970\n")
plt.xlabel('Year')
plt.ylabel('Unemployment rate')
plt.show()

#plot the graph showing the variation of GDP for 4 countries selected
plt.plot(India_data['Year'],India_data['GDP in USD'])
plt.plot(USA_data['Year'],USA_data['GDP in USD'])
plt.plot(China_data['Year'],China_data['GDP in USD'])
plt.plot(Ireland_data['Year'],Ireland_data['GDP in USD'])
plt.legend(['India', 'USA','China','Ireland'], loc='best')
plt.title("GDP aross all major countries since 1970\n")
plt.xlabel('Year')
plt.ylabel('GDP in USD')
plt.show()

plt.scatter(dataUSA['GDP in USD'],dataUSA['Unemployment(%)'] )
plt.title('GDP against Unemployment(%) in USA')
plt.xlabel('GDP in USD')
plt.ylabel('Unemployment(%)')
plt.show()

plt.scatter(India_data['GDP in USD'],India_data['Unemployment(%)'] )
plt.title('GDP against Unemployment(%) in India')
plt.xlabel('GDP in USD')
plt.ylabel('Unemployment(%)')
plt.show()

plt.scatter(Ireland_data['GDP in USD'],Ireland_data['Unemployment(%)'] )
plt.title('GDP against Unemployment(%) in Ireland')
plt.xlabel('GDP in USD')
plt.ylabel('Unemployment(%)')
plt.show()
