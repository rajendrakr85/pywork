
import pandas as pd

data =[{'name': 'John', 'age': 29,'Sex':'Male', 'department': 'HR', 'salary': 60000, 'join_date': '2015-03-25'},
    {'name': 'Alice', 'age': 35,'Sex':'Male', 'department': 'IT', 'salary': 80000, 'join_date': '2018-06-01'},
    {'name': 'Bob', 'age': 40,'Sex':'Male', 'department': 'Finance', 'salary': 75000, 'join_date': '2016-09-14'},
    {'name': 'Emma', 'age': 28,'Sex':'Female', 'department': 'IT', 'salary': 90000, 'join_date': '2020-05-30'},
    {'name': 'Chris', 'age': 20,'Sex':'Male', 'department': 'HR', 'salary': 85000, 'join_date': '2012-07-11'},
    {'name': 'David', 'age': 33,'Sex':'Male', 'department': 'Finance', 'salary': 95000, 'join_date': '2014-04-19'},
    {'name': 'Sophia', 'age': 31,'Sex':'Female', 'department': 'IT', 'salary': 78000, 'join_date': '2019-03-22'},
    {'name': 'James', 'age': 37,'Sex':'Male', 'department': 'Finance', 'salary': 105000, 'join_date': '2017-11-09'},
    {'name': 'Olivia', 'age': 12,'Sex':'Female', 'department': 'HR', 'salary': 62000, 'join_date': '2021-02-11'}
]

#filter employee by age ge no
#find average salary dept wise
df = pd.DataFrame(data, index=['a','b','c','d','e','f','g','h','i'])
df['join_date'] = pd.to_datetime(df['join_date'])
#How many male and female employees are there in the organization?
#print(df.groupby('Sex')['Sex'].agg('count'))
#Print the name of all departments in the organization?
#print(df['department'].unique())
#What is the average age of male and female employees?
#print(df.groupby('Sex')['age'].mean())
#Get the details of highest paid employee in the organization?
#print(df.sort_values(by='salary',ascending=False).iloc[0])
#print(df.loc[df['salary'].idxmax()])
#Get the names of all employees who have joined after 2015?
#print(df[df['join_date'] > '2015-12-31'][['join_date','name']])
# Count the number of employees in each department?
#print(df.groupby('department')['department'].count())
#Get the details of youngest male employee in the product development department?
idm = df[(df['Sex']=='Male') & (df['department']=='HR')].sort_values(by='age', ascending=True).iloc[0]
print(idm)
#print(idmf[['name','age','department']])
#How many male and female employees are there in the sales and marketing team?
fdf = df[(df['department'] == 'HR') | (df['department']=='IT')]
#print(fdf.groupby('Sex').size().reset_index(name='Count'))
#What is the average salary of male and female employees?
#print(df.groupby('Sex')['salary'].mean())
#List down the names of all employees in each department?
#print(df.groupby('department')['name'].apply(list).reset_index(name='Emp Name'))
#What is the average salary and total salary of the whole organization?
#print(df['salary'].sum())
#print(df['salary'].mean())
#Separate the employees who are younger or equal to 25 years from those employees who are older than 25 years.
# print(df[df['age']<=25],end='\n')
# print()
# print(df[df['age']>25], end='\n')
#Who is the oldest employee in the organization? What is his age and which department he belongs to?
#oldf = df[df['age'] == df['age'].max()][['name','age', 'department']]
#print(oldf)
#print(df.groupby(['department'])['age'].min())
#print(df.groupby('department')['salary'].agg('mean'))
#print(df.iloc[[0,1],[3,2]])
#print(df.query("age >=30").query("department=='HR'"))
#print(df.groupby('department')['salary'].sum())
#print(df.groupby('department').agg('salary').mean())
# print(age_df)
# saldf = df.groupby("department")["salary"].sum()
# print(saldf)
# dd = df.groupby('department')['salary'].agg('mean')
# print(dd)








