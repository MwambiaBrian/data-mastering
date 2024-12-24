import pandas as pd


# Series
def createSeries (data: list) -> pd.Series:
    series = pd.Series(data, name="Marks")
    return series


#series_data = [1,3,5,7,8]
#print(createSeries(series_data))
# DataFrame
def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    columns = ['student_id', 'age']
    df = pd.DataFrame(student_data, columns=columns)    
    return df      
student_data =[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

#print(createDataframe(student_data))

# Get the Size of a DataFrame

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return list(players.shape)

#print(getDataframeSize(createDataframe(student_data)))

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [25, 30, 35, 28, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
}
df=pd.DataFrame(data)
def selectFirstRow(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

print(selectFirstRow(df))