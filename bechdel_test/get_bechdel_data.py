import requests
import pandas as pd

url = 'http://bechdeltest.com/api/v1/getAllMovies'
req = requests.get(url)

data = req.json()
df = pd.DataFrame(data)

df.to_csv('bechdel.csv', index = False)