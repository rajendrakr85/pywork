import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Score': [88, 95, 70, 89]
}
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
#print(df.loc[['a','b']])  # Selects the row with index 'a'


li=[23,34,45,56]
for i in range(2,len(li)):
    print(li[i])

